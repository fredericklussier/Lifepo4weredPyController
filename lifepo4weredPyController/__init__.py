#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .Battery import Battery
from .LedStateEnum import ledStateEnum
from .Led import Led
from .USBPowerSource import USBPowerSource
from .Reader import Reader

__author__ = "Frederick Lussier <frederick.lussier@hotmail.com>"
__status__ = "dev"
__version__ = "0.1.0"
__date__ = "september 10th 2017"

__all__ = ["Battery", "USBPowerSource", "Led", "ledStateEnum"]

battery = Battery()
led = Led()
usbPowerSource = USBPowerSource()

__reader = Reader()
__reader.add(battery._read)
__reader.add(usbPowerSource._read)
__reader.read()


def ceaseReading():
    __reader.stop()

# TOUCH...
# VOUT
# VOUT_MAX
# AUTO_BOOT and rest...
