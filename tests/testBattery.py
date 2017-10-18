#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import unittest
from unittest.mock import patch

from tests import mockLifepo4weredSO
import lifepo4weredPyController


class BatteryTests(unittest.TestCase):
    """
    voltage
    """

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=3354)
    def testVoltage_ShouldGetVoltage(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.battery.voltage

        # Assert
        self.assertEqual(actualValue, 3354)

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    def testVoltage_waitReading_ShouldGetVoltage(self):
        # Arrange
        handleCalled = False
        count = 0

        # Action
        @lifepo4weredPyController.battery.observeElement("voltage")
        def voltageChangeHandle(previous, actual):
            nonlocal count, handleCalled
            handleCalled = True
            self.assertEqual(actual, 10)

        while count < 3:
            count += 1
            time.sleep(0.5)

        lifepo4weredPyController.battery.unObserve("voltage",
                                                   voltageChangeHandle)

        # Assert
        self.assertTrue(handleCalled)

    """
    rate
    """

    def readSideEffects(value):
        """
        Simulate returned value when reading the data
        variable from the lifepo4weredSO
        """
        if value == 10:  # VBAT
            return 3392

        elif value == 13:  # VBAT_SHDN
            return 2950  # according to Lifepo4weredPi documentation

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered',
           side_effect=readSideEffects)
    def testRate_3392Volt_ShouldReturn1(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.battery.rate

        # Assert
        self.assertEqual(actualValue, 1)

    def readShutDowndSideEffects(value):
        """
        Simulate returned value when reading the data
        variable from the lifepo4weredSO
        """
        if value == 10:  # VBAT
            return 2950

        elif value == 13:  # VBAT_SHDN
            return 2950  # according to Lifepo4weredPi documentation

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered',
           side_effect=readShutDowndSideEffects)
    def testRate_2950Volt_ShouldReturn0(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.battery.rate

        # Assert
        self.assertEqual(actualValue, 0.0)

    def readGreatherThanFULLSideEffects(value):
        """
        Simulate returned value when reading the data
        variable from the lifepo4weredSO
        """
        if value == 10:  # VBAT
            return 3400

        elif value == 13:  # VBAT_SHDN
            return 2950  # according to Lifepo4weredPi documentation

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered',
           side_effect=readGreatherThanFULLSideEffects)
    def testRate_3300Volt_ShouldReturn1(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.battery.rate

        # Assert
        self.assertEqual(actualValue, 1)

    def readSmallerThanSHDNSideEffects(value):
        """
        Simulate returned value when reading the data
        variable from the lifepo4weredSO
        """
        if value == 10:  # VBAT
            return 2000

        elif value == 13:  # VBAT_SHDN
            return 2950  # according to Lifepo4weredPi documentation

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered',
           side_effect=readSmallerThanSHDNSideEffects)
    def testRate_2000Volt_ShouldReturn0(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.battery.rate

        # Assert
        self.assertEqual(actualValue, 0)

    def readHalfSideEffects(value):
        """
        Simulate returned value when reading the data
        variable from the lifepo4weredSO
        """
        if value == 10:  # VBAT
            return 3171

        elif value == 13:  # VBAT_SHDN
            return 2950  # according to Lifepo4weredPi documentation

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered',
           side_effect=readHalfSideEffects)
    def testRate_waitReading_ShouldReturnHalf(self, mockedLib):
        # Arrange
        handleCalled = False
        count = 0

        # Action
        @lifepo4weredPyController.battery.observeElement("rate")
        def rateChangeHandle(previous, actual):
            nonlocal count, handleCalled
            handleCalled = True
            self.assertEqual(actual, 0.5)

        while count < 3:
            count += 1
            time.sleep(0.5)

        lifepo4weredPyController.battery.unObserve("rate",
                                                   rateChangeHandle)

        # Assert
        self.assertTrue(handleCalled)
