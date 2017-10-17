#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import unittest
from unittest.mock import patch

from tests import mockLifepo4weredSO
import lifepo4weredPyController


class BatteryTests(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        lifepo4weredPyController.ceaseReading()

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
        def batteryVoltageHandle(previous, actual):
            nonlocal count, handleCalled
            handleCalled = True
            self.assertEqual(actual, 10)

        while count < 3:
            count += 1
            time.sleep(0.5)

        # Assert
        self.assertTrue(handleCalled)
