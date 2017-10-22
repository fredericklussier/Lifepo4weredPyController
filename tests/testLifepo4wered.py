#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import unittest
from unittest.mock import patch

from tests import mockLifepo4weredSO
import lifepo4weredPyController


class Lifepo4weredTests(unittest.TestCase):

    """
    Wait State changes
    """

    def readDataSideEffects(value):
        """
        Simulate returned value when reading the data
        variable from the lifepo4weredSO
        """
        if value == 10:  # VBAT
            return 3100

        elif value == 13:  # VBAT_SHDN
            return 2950  # according to Lifepo4weredPi documentation

        elif value == 9:  # VIN
            return 0

        elif value == 3:  # TOUCH_STATE
            return 0

        else:
            return 10

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered',
           side_effect=readDataSideEffects)
    def testDiffuse_waitReading_ShouldReturnState(self, mockedLib):
        # Arrange
        handleCalled = False
        count = 0

        # Action
        @lifepo4weredPyController.lifepo4wered.observeState()
        def lifepo4weredStateChangeHandle(previous, actual):
            nonlocal count, handleCalled
            handleCalled = True
            self.assertEqual(
                actual,
                {
                    "batteryVoltage": 3100,
                    "batteryRate": 0.3393665158371041,
                    "usbPowerSourceVoltage": 0,
                    "usbPowerSourcePluggedIn": False,
                    "touchState":
                        lifepo4weredPyController.touchStateEnum.inactive
                })

        while count < 3:
            count += 1
            time.sleep(0.5)

        lifepo4weredPyController.lifepo4wered.unObserve(
            "*",
            lifepo4weredStateChangeHandle)

        # Assert
        self.assertTrue(handleCalled)