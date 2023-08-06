"""Helpers to deal with Cast devices."""
from __future__ import annotations

from typing import Optional

import attr
from pychromecast import dial
from pychromecast.const import CAST_TYPE_GROUP

DEFAULT_PORT = 8009


@attr.s(slots=True, frozen=True)
class ChromecastInfo:
    """
    Class to hold all data about a chromecast for creating connections.

    This also has the same attributes as the mDNS fields by zeroconf.
    """

    services: set | None = attr.ib()
    uuid: str = attr.ib(converter=attr.converters.optional(str))
    model_name: str = attr.ib()
    friendly_name: str = attr.ib()
    cast_type: str = attr.ib()
    manufacturer: str = attr.ib()
    is_dynamic_group = attr.ib(type=Optional[bool], default=None)

    @property
    def is_audio_group(self) -> bool:
        """Return if the cast is an audio group."""
        return self.cast_type == CAST_TYPE_GROUP

    def fill_out_missing_chromecast_info(self, zconf) -> ChromecastInfo:
        """
        Return a new ChromecastInfo object with missing attributes filled in.

        Uses blocking HTTP / HTTPS.
        """
        if not self.is_audio_group or self.is_dynamic_group is not None:
            # We have all information, no need to check HTTP API.
            return self

        # Fill out missing group information via HTTP API.
        is_dynamic_group = False
        http_group_status = None
        http_group_status = dial.get_multizone_status(
            None,
            services=self.services,
            zconf=zconf,
        )
        if http_group_status is not None:
            is_dynamic_group = any(
                str(g.uuid) == self.uuid for g in http_group_status.dynamic_groups
            )

        return ChromecastInfo(
            services=self.services,
            uuid=self.uuid,
            friendly_name=self.friendly_name,
            model_name=self.model_name,
            cast_type=self.cast_type,
            manufacturer=self.manufacturer,
            is_dynamic_group=is_dynamic_group,
        )

    def __str__(self):
        """Return pretty printable string for logging."""
        return f"{self.friendly_name} ({self.uuid})"


class CastStatusListener:
    """
    Helper class to handle pychromecast status callbacks.

    Necessary because a CastDevice entity can create a new socket client
    and therefore callbacks from multiple chromecast connections can
    potentially arrive. This class allows invalidating past chromecast objects.
    """

    def __init__(self, cast_device, chromecast, mz_mgr, mz_only=False):
        """Initialize the status listener."""
        self._cast_device = cast_device
        self._uuid = chromecast.uuid
        self._valid = True
        self._mz_mgr = mz_mgr

        if cast_device._cast_info.is_audio_group:
            self._mz_mgr.add_multizone(chromecast)
        if mz_only:
            return

        chromecast.register_status_listener(self)
        chromecast.socket_client.media_controller.register_status_listener(self)
        chromecast.register_connection_listener(self)
        if not cast_device._cast_info.is_audio_group:
            self._mz_mgr.register_listener(chromecast.uuid, self)

    def new_cast_status(self, cast_status):
        """Handle reception of a new CastStatus."""
        if self._valid:
            self._cast_device.new_cast_status(cast_status)

    def new_media_status(self, media_status):
        """Handle reception of a new MediaStatus."""
        if self._valid:
            self._cast_device.new_media_status(media_status)

    def new_connection_status(self, connection_status):
        """Handle reception of a new ConnectionStatus."""
        if self._valid:
            self._cast_device.new_connection_status(connection_status)

    @staticmethod
    def added_to_multizone(group_uuid):
        """Handle the cast added to a group."""

    def removed_from_multizone(self, group_uuid):
        """Handle the cast removed from a group."""
        if self._valid:
            self._cast_device.multizone_new_media_status(group_uuid, None)

    def multizone_new_cast_status(self, group_uuid, cast_status):
        """Handle reception of a new CastStatus for a group."""

    def multizone_new_media_status(self, group_uuid, media_status):
        """Handle reception of a new MediaStatus for a group."""
        if self._valid:
            self._cast_device.multizone_new_media_status(group_uuid, media_status)

    def invalidate(self):
        """
        Invalidate this status listener.

        All following callbacks won't be forwarded.
        """
        # pylint: disable=protected-access
        if self._cast_device._cast_info.is_audio_group:
            self._mz_mgr.remove_multizone(self._uuid)
        else:
            self._mz_mgr.deregister_listener(self._uuid, self)
        self._valid = False
