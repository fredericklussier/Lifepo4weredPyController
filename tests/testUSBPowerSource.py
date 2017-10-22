#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import unittest
from unittest.mock import patch

from tests import mockLifepo4weredSO
import lifepo4weredPyController


class USBPowerSourceTests(unittest.TestCase):

    """
    voltage
    """

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=5000)
    def testVoltage_ShouldGetVoltage(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.usbPowerSource.voltage

        # Assert
        self.assertEqual(actualValue, 5000)

    def readVoltageSideEffects(value):
        """
        Simulate returned value when reading the data
        variable from the lifepo4weredSO
        """
        if value == 10:  # VBAT
            return 3300

        elif value == 13:  # VBAT_SHDN
            return 2950  # according to Lifepo4weredPi documentation

        elif value == 9:  # VIN
            return 5020

        elif value == 3:  # TOUCH_STATE
            return 0

        else:
            return 10

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered',
           side_effect=readVoltageSideEffects)
    def testVoltage_waitReading_ShouldGetVoltage(self, mockedLib):
        # Arrange
        handleCalled = False
        count = 0

        # Action
        @lifepo4weredPyController.usbPowerSource.observeElement("voltage")
        def voltageChangeHandle(previous, actual):
            nonlocal count, handleCalled
            handleCalled = True
            self.assertEqual(actual, 5020)

        while count < 3:
            count += 1
            time.sleep(0.5)

        lifepo4weredPyController.usbPowerSource.unObserve("voltage",
                                                          voltageChangeHandle)

        # Assert
        self.assertTrue(handleCalled)

    """
    plugged
    """

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=5000)
    def testPluggedIn_WhenConnected_ShouldrReturnTrue(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.usbPowerSource.pluggedIn

        # Assert
        self.assertTrue(actualValue)

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0)
    def testPluggedIn_WhenUnconnected_ShouldrReturnFalse(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.usbPowerSource.pluggedIn

        # Assert
        self.assertFalse(actualValue)

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    def testPluggedIn_waitReading_ShouldGetPluggedIn(self):
        # Arrange
        handleCalled = False
        count = 0

        # Action
        @lifepo4weredPyController.usbPowerSource.observeElement("pluggedIn")
        def USBPlugChangeHandle(previous, actual):
            nonlocal count, handleCalled
            handleCalled = True
            self.assertTrue(actual)

        while count < 3:
            count += 1
            time.sleep(0.5)

        lifepo4weredPyController.usbPowerSource.unObserve("pluggedIn",
                                                          USBPlugChangeHandle)

        # Assert
        self.assertTrue(handleCalled)
