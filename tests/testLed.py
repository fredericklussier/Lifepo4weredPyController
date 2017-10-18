#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import unittest
from unittest.mock import patch

from tests import mockLifepo4weredSO
import lifepo4weredPyController


class LedTests(unittest.TestCase):

    """
    State
    """

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x00)
    def testState_ShouldReturnOff(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.led.state

        # Assert
        self.assertEqual(actualValue,
                         lifepo4weredPyController.ledStateEnum.off)

    """
    On
    """
    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x01)
    def testState_ShouldReturnOn(self, mockedLib):
        # Arrange

        # Action
        lifepo4weredPyController.led.on()
        actualValue = lifepo4weredPyController.led.state

        # Assert
        self.assertEqual(actualValue,
                         lifepo4weredPyController.ledStateEnum.on)

    """
    Off
    """
    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x00)
    def testState_ShouldReturnOn(self, mockedLib):
        # Arrange
        lifepo4weredPyController.led.on()

        # Action
        lifepo4weredPyController.led.off()
        actualValue = lifepo4weredPyController.led.state

        # Assert
        self.assertEqual(actualValue,
                         lifepo4weredPyController.ledStateEnum.off)

    """
    pulse
    """
    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x02)
    def testState_ShouldReturnPulse(self, mockedLib):
        # Arrange

        # Action
        lifepo4weredPyController.led.pulse()
        actualValue = lifepo4weredPyController.led.state

        # Assert
        self.assertEqual(actualValue,
                         lifepo4weredPyController.ledStateEnum.pulsing)

    """
    flash
    """
    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x03)
    def testState_ShouldReturnFlash(self, mockedLib):
        # Arrange

        # Action
        lifepo4weredPyController.led.flash()
        actualValue = lifepo4weredPyController.led.state

        # Assert
        self.assertEqual(actualValue,
                         lifepo4weredPyController.ledStateEnum.flasing)

    """
    Raise Error
    """
    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x0C)
    def testState_Bad_ShouldRaiseError(self, mockedLib):
        # Arrange: return 0x0C by the mock as led state is an error

        # Action & Assert
        with self.assertRaises(ValueError):
            actualValue = lifepo4weredPyController.led.state
