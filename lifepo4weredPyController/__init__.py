#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .Battery import Battery
from .LedStateEnum import ledStateEnum
from .Led import Led
from .USBPowerSource import USBPowerSource
from .Touch import Touch
from .Reader import Reader

__author__ = "Frederick Lussier <frederick.lussier@hotmail.com>"
__status__ = "dev"
__version__ = "0.1.0"
__date__ = "september 10th 2017"

__all__ = ["Battery", "USBPowerSource", "Led", "ledStateEnum", "Touch"]

battery = Battery()
led = Led()
usbPowerSource = USBPowerSource()

__reader = Reader()
__reader.add(battery._diffuseChanges)
__reader.add(usbPowerSource._diffuseChanges)
__reader.read()


def setPeriodicInterval(interval):
    """
    Set the interval between read data from power supply board

    :param number interval: delay in second
    """
    __reader.interval = interval


def ceaseReading():
    """
    Cease reading data from power supply board.

    This is important when you close your application.
    """
    __reader.stop()

# TOUCH...
# VOUT
# VOUT_MAX
# AUTO_BOOT and rest...
