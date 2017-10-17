#!/usr/bin/python3
# -*- coding: utf-8 -*-

from observablePy import Observable, observable_property
import lifepo4weredPy
import copy


class Touch(Observable):
    def __init__(self):
        super(Touch, self).__init__()
        self.instanceState = {
            "state": 0,
        }

        self.addObservableElement("state")

    @property
    def state(self):
        return lifepo4weredPy.read(lifepo4weredPy.variablesEnum.TOUCH_STATE)

    def _diffuseChanges(self):
        if self.hasObservers():
            state = self.state

            if (voltage != self.instanceState["state"]):
                previousState = copy.deepcopy(self.instanceState)

                self.instanceState["state"] = state

                self.diffuse(previousState, self.instanceState)
