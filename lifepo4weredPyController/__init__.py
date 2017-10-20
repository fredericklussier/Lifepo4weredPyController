#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .packageInfo import AUTHOR, VERSION, STATUS

from .packageExposedServices import (
    battery, led, touch, wakeTimer, usbPowerSource,
    ledStateEnum, touchStateEnum,
    getPeriodicInterval, setPeriodicInterval, ceaseReading, restartReading)

__author__ = AUTHOR
__status__ = STATUS
__version__ = VERSION
__date__ = "september 10th 2017"

__all__ = [
    "battery",
    "usbPowerSource",
    "led", "ledStateEnum",
    "touch", "touchStateEnum",
    "wakeTimer"
]
