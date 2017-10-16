#!/usr/bin/python3
# -*- coding: utf-8 -*-

from observablePy import Observable, observable_property
import lifepo4weredPy
import copy

BATTERY_FULL = 3392  # mVolt


class Battery(Observable):
    def __init__(self):
        super(Battery, self).__init__()
        self.state = {
            "voltage": 0,
            "level": 0.0,
        }

        self.addObservableElement("voltage")
        self.addObservableElement("rate")

    @property
    def voltage(self):
        return lifepo4weredPy.read(lifepo4weredPy.variablesEnum.VBAT)

    @property
    def rate(self):
        return self._computeRate(self.voltage, self.shutdownVoltage)

    def _computeRate(self, actualVoltage, shutdownVoltage):
        batteryNomalizedVolt = (actualVoltage
                                if actualVoltage < BATTERY_FULL
                                else BATTERY_FULL) - shutdownVoltage

        if ((BATTERY_FULL - shutdownVoltage) == 0):
            return 0
        else:
            return batteryNomalizedVolt / (BATTERY_FULL - shutdownVoltage)

    @observable_property
    def shutdownVoltageLevel(self):
        return lifepo4weredPy.read(lifepo4weredPy.variablesEnum.VBAT_SHDN)

    @shutdownVoltageLevel.setter
    def shutdownVoltageLevel(self, value):
        return lifepo4weredPy.write(lifepo4weredPy.variablesEnum.VBAT_SHDN,
                                    value)

    @observable_property
    def emergencyShutdownVoltageLevel(self):
        return lifepo4weredPy.read(lifepo4weredPy.variablesEnum.VBAT_MIN)

    @emergencyShutdownVoltageLevel.setter
    def emergencyShutdownVoltageLevel(self, value):
        return lifepo4weredPy.write(lifepo4weredPy.variablesEnum.VBAT_MIN,
                                    value)

    @observable_property
    def allowedToBootVoltageLevel(self):
        return lifepo4weredPy.read(lifepo4weredPy.variablesEnum.VBAT_BOOT)

    @allowedToBootVoltageLevel.setter
    def allowedToBootVoltageLevel(self, value):
        return lifepo4weredPy.write(lifepo4weredPy.variablesEnum.VBAT_BOOT,
                                    value)

    def _read(self):
        if self.hasObservers():
            previousState = copy.deepcopy(self.state)

            self.state["voltage"] = self.voltage
            self.state["rate"] = self._computeRate(self.state["voltage"],
                                                   self.shutdownVoltageLevel)

            self.diffuse(previousState, self.state)
