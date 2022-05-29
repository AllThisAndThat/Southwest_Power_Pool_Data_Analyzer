#!/usr/bin/env python
'''Class that stores time and load information'''
__author__ = "Lucas Hudson"
__email__ = "lucaslorenhudson@gmail.com"
__status__ = "Prototype"

class LOAD_TIME:
    def __init__(self, *, year, month, day, hour, load):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.load = load

    def __init__(self, time_string, load_string):
        self.year = int(time_string[6:10])
        self.month = int(time_string[3:5])
        self.day = int(time_string[0:2])
        self.hour = int(time_string[11:13])
        self.load = float(load_string)

    def load_print(self):
        print("%d\%d\%d %d:00 : %.3fMWH"%
            (self.month, self.day, self.year, self.hour, self.load))
