from enum import Enum
import math


class Days(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class Time():

    def __init__(self, hour=0, min=0):
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

    @property
    def hour(self):
        return self._hour

    @min.setter
    def hour(self, val):
        if val >= 0 and val <= 24:
            self._min = val
        else:
            self._min = 0

    def __str__(self):
        return 'Time- {} : {}'.format(self._hour, self._min)


class Movie():

    def __init__(self, title, duration_min) -> None:
        self._title = title
        self._duration_min = duration_min

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title = val

    @property
    def duration_min(self):
        return self._duration_min

    @title.setter
    def duration_min(self, val):
        self._duration_min = val

    def __str__(self) -> str:
        return 'Movie name : {} Duration : {}'.format(self._title, self._duration_min)


# Movie movie, Time startTime, Time endTime;
class Seance:

    def __init__(self, movie: Movie, start_time: Time):
        self.movie = movie
        self.start_time = start_time
        self.end_time = None

    def _end_time_calculation(self):
        hour = math.floor((self.start_time.min + self.movie.duration_min) / 60)
        min = hour * 60 - (self.start_time.min + self.movie.duration_min) / 60
        self.end_time = Time(min, hour)
