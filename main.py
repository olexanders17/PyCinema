from enum import Enum


class Days(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class Time():

    def __init__(self, min=0, hour=0):
        self.min = min
        self.hour = hour


time=Time()