#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tinyPeriodicTask


class Reader():
    def __init__(self):
        self.jobs = []
        self.__task = {}

    def __del__(self):
        self.__task.stop()
        self.__task = None

    def add(self, job):
        self.jobs.append(job)

    def read(self):
        def _read():
            for job in self.jobs:
                job()

        self.__task = tinyPeriodicTask.TinyPeriodicTask(1, _read)
        self.__task.start()

    def stop(self):
        self.__task.stop()