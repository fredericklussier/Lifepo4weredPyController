#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import unittest
from unittest.mock import patch

from tests import mockLifepo4weredSO
import lifepo4weredPyController


class WakeTimerTests(unittest.TestCase):

    """
    state
    """
    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=60)
    def testState_ShouldReturnInactive(self, mockedLib):
        # Arrange
        # Action
        actualValue = lifepo4weredPyController.wakeTimer.wakeUp

        # Assert
        self.assertEqual(actualValue, 60)

    @patch('lifepo4weredPy.functions.lifepo4weredSO', new=mockLifepo4weredSO)
    @patch('tests.mockLifepo4weredSO.read_lifepo4wered', return_value=3600)
    def testState_ShouldReturnInactive(self, mockedLib):
        # Arrange
        # Action
        lifepo4weredPyController.wakeTimer.wakeUp = 3600
        actualValue = lifepo4weredPyController.wakeTimer.wakeUp

        # Assert
        self.assertEqual(actualValue, 3600)
