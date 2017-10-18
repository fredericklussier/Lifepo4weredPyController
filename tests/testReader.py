#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import unittest
from unittest.mock import patch

from tests import mockLifepo4weredSO
import lifepo4weredPyController


class ReaderTests(unittest.TestCase):

    """
    tearDown each test
    """

    def tearDown(self):
        lifepo4weredPyController.setPeriodicInterval(0.5)
        lifepo4weredPyController.restartReading()

    """
    Interval
    """

    def testInterval_Set_ShouldChangeInterval(self):
        # Arrange
        # Action
        lifepo4weredPyController.setPeriodicInterval(5)

        # Assert
        self.assertEqual(lifepo4weredPyController.getPeriodicInterval(), 5)

    """
    Cease
    """
    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    def testCease_ShouldCeaseReading(self):
        # Arrange
        handleCalled = False
        count = 0

        @lifepo4weredPyController.battery.observeElement("voltage")
        def voltageChangeHandle(previous, actual):
            nonlocal handleCalled
            handleCalled = True

        # Action
        lifepo4weredPyController.ceaseReading()

        while count < 3:
            count += 1
            time.sleep(0.5)

        lifepo4weredPyController.battery.unObserve("voltage",
                                                   voltageChangeHandle)

        # Assert
        self.assertFalse(handleCalled)
