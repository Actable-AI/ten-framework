"""
Blaze Realtime STT Extension for TEN Framework

This extension provides realtime (streaming) Speech-to-Text (STT) functionality
using the Blaze realtime WebSocket API.
Implements the TEN framework extension interface.
"""

from .blaze_stt_realtime import (
    BlazeSTTRealtimeConfig,
    BlazeSTTRealtimeExtension,
)

__all__ = ["BlazeSTTRealtimeExtension", "BlazeSTTRealtimeConfig"]
__version__ = "1.0.0"
