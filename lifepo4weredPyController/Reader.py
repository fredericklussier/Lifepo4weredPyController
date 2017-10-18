#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tinyPeriodicTask


class Reader():
    def __init__(self):
        self.jobs = []
        self.__task = {}

    @property
    def interval(self):
        return self.__task.interval

    @interval.setter
    def interval(self, value):
        self.__task.interval = value

    def add(self, job):
        self.jobs.append(job)

    def startPeriodicallyReading(self):
        def _readJobs():
            for job in self.jobs:
                job()

        self.__task = tinyPeriodicTask.TinyPeriodicTask(0.5, _readJobs)
        self.__task.start()

    def restart(self):
        self.__task.start()

    def stop(self):
        self.__task.stop()
