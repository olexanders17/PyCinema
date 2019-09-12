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
        self._min = min
        self._hour = hour

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, val):
        if val >= 0 and val <= 59:
            self._min = val
        else:
            self._min = 0

    def __str__(self):
        return 'Time- {} : {}'.format(self._hour, self._min)


#


time = Time(10, 56)
print(time)
