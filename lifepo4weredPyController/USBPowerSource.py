#!/usr/bin/python3
# -*- coding: utf-8 -*-

from observablePy import Observable, observable_property
import lifepo4weredPy


class USBPowerSource(Observable):
    def __init__(self):
        super(USBPowerSource, self).__init__()
        self.state = {
          "voltage": 0,
          "pluggedIn": False,
        }
        self.addObservableElement("voltage")
        self.addObservableElement("pluggedIn")

    @property
    def voltage(self):
        return lifepo4weredPy.read(lifepo4weredPy.variablesEnum.VIN)

    @property
    def pluggedIn(self):
        return lifepo4weredPy.read(lifepo4weredPy.variablesEnum.VIN) > 0

    @observable_property
    def allowedToBootVoltageLevel(self):
        return lifepo4weredPy.read(lifepo4weredPy.variablesEnum.VIN_THRESHOLD)

    @allowedToBootVoltageLevel.setter
    def allowedToBootVoltageLevel(self, value):
        return lifepo4weredPy.write(lifepo4weredPy.variablesEnum.VIN_THRESHOLD,
                                    value)

    def _read(self):
        if self.hasObservers():
            previousState = copy.deepcopy(self.state)

            self.state["voltage"] = self.voltage
            self.state["pluggedIn"] = (self.voltage > 0)

            self.diffuse(previousState, self.state)
