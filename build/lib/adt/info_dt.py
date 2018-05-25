# Class that provides setting the time range
# User will get information in the time-range frames
# Date available from 01.01.2014 to today

from datetime import datetime, timedelta
from adt.visualization import Visualize


class IncorrectDateError(Exception):
    pass


class InformationADT(Visualize):
    """
    Represents the information on abstract topic
    """

    def __init__(self):
        self.start = None
        self.end = None
        super().__init__()

    def _valid(self, y, m, d):
        """
        (int, int, int) -> bool
        y, m, d: the date in form year/month/day
        return: True if date is correct
        """
        print(y, m, d)
        current = datetime(y, m, d)
        try:
            if datetime(2008, 1, 1) <= current < datetime(2018, 1, 1):
                return current
            else:
                raise IncorrectDateError('Enter the date between 01.01.2014 and '
                                         'today')
        except ValueError:
            print('Incorrect date')

    def set_start(self, y, m, d):
        """
        (int, int, int) -> none
        Setting the start
        y, m, d: the date in form year/month/day
        """
        start = self._valid(y, m, d)
        if not self.end or start <= self.end:
            self.start = start
        else:
            raise IncorrectDateError('The start cannot be before the end')

    def set_end(self, y, m, d):
        """
        (int, int, int) -> none
        Setting the end
        y, m, d: the date in form year/month/day
        """
        end = self._valid(y, m, d)
        if not self.start or self.start <= end:
            self.end = end
        else:
            raise IncorrectDateError('The start cannot be before the end')

    def _time_range(self):
        """
        Created to iterate days in range between the start and the end
        return: day
        """
        assert self.start and self.end, 'Set up the start and the end before'
        dlt = self.end - self.start
        for i in range(dlt.days + 1):
            day = self.start + timedelta(days=i)
            yield day
