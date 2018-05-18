# Was created to collect the information from different API by year
# Years available from 2014 to today

import json
from datetime import datetime


class IncorrectDateError(Exception):
    pass


class SaveInformationADT:
    """
    Process saving of the information
    """

    MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
              '11', '12']

    def __init__(self, year, region=None):
        self.year = year
        self.region = region
        self.changes = {}

    @staticmethod
    def _is_valid(year):
        """
        year: int, information date year
        return: True if year is between 2014 and today, False otherwise
        """
        if isinstance(year, int) and 2014 <= year < datetime.today().year:
            return True
        raise IncorrectDateError

    def generate(self):
        raise NotImplementedError

    def save(self, path):
        """
        Saving information to the special file
        """
        with open(path, 'w') as outfile:
            json.dump(self.changes, outfile)
