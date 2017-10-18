#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import unittest
from unittest.mock import patch

from tests import mockLifepo4weredSO
import lifepo4weredPyController


class TouchTests(unittest.TestCase):

    """
    state
    """
    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x00)
    def testState_ShouldReturnInactive(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.touch.state

        # Assert
        self.assertEqual(actualValue,
                         lifepo4weredPyController.touchStateEnum.inactive)

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x03)
    def testState_ShouldReturnStart(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.touch.state

        # Assert
        self.assertEqual(actualValue,
                         lifepo4weredPyController.touchStateEnum.start)

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x0C)
    def testState_ShouldReturnStop(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.touch.state

        # Assert
        self.assertEqual(actualValue,
                         lifepo4weredPyController.touchStateEnum.stop)

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x0F)
    def testState_ShouldReturnHeld(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.touch.state

        # Assert
        self.assertEqual(actualValue,
                         lifepo4weredPyController.touchStateEnum.held)

    """
    Observer
    """
    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x03)
    def testState_waitReading_ShouldGetState(self, mockedLib):
        # Arrange
        handleCalled = False
        count = 0

        # Action
        @lifepo4weredPyController.touch.observeElement("state")
        def stateChangeHandle(previous, actual):
            nonlocal count, handleCalled
            handleCalled = True
            self.assertEqual(actual,
                             lifepo4weredPyController.touchStateEnum.start)

        while count < 3:
            count += 1
            time.sleep(0.5)

        lifepo4weredPyController.touch.unObserve("state", stateChangeHandle)

        # Assert
        self.assertTrue(handleCalled)

    """
    Raise Error
    """
    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=0x05)
    def testState_Bad_ShouldRaiseError(self, mockedLib):
        # Arrange: return 0x05 by the mock as touch state is an error

        # Action & Assert
        with self.assertRaises(ValueError):
            actualValue = lifepo4weredPyController.touch.state
