#  Copyright (C) 2019-2021 Parrot Drones SAS
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the Parrot Company nor the names
#    of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#  PARROT COMPANY BE LIABLE FOR ANY DIRECT, INDIRECT,
#  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
#  OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
#  AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
#  OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
#  SUCH DAMAGE.

import olympe.module_loader
from .arsdkng.events import ArsdkMessageEvent
from .controller import Drone, SkyController
from .event import Event
from .expectations import Expectation
from .listener import EventListener, listen_event
from .media import Media, MediaEvent, MediaInfo, ResourceInfo
from .video import VMetaFrameType
from .video.frame import VideoFrame
from .video.pdraw import PdrawState, Pdraw
import olympe.messages  # noqa
import olympe.enums  # noqa
import olympe.log  # noqa

from .utils import hashabledict
from .__version__ import __version__
import olympe_deps as od
from olympe_deps import vdef_i420
from olympe_deps import vdef_nv12

VDEF_I420 = hashabledict(od.struct_vdef_raw_format.as_dict(vdef_i420))
VDEF_NV12 = hashabledict(od.struct_vdef_raw_format.as_dict(vdef_nv12))

__version__ = __version__

__all__ = [
    "ArsdkMessageEvent",
    "Drone",
    "Event",
    "EventListener",
    "Expectation",
    "Media",
    "MediaEvent",
    "MediaInfo",
    "Pdraw",
    "PdrawState",
    "ResourceInfo",
    "SkyController",
    "VDEF_I420",
    "VDEF_NV12",
    "VMetaFrameType",
    "VideoFrame",
    "listen_event",
]
