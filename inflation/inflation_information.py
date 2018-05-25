from adt.info_dt import InformationADT
import json


class Inflation(InformationADT):
    """
    Represents abstract DT for getting CPI rates
    """

    def __init__(self, path):
        super().__init__()
        self.path = 'inflation/' + path

    def generate(self):
        """
        Generating all data from start date to end date
        """
        all_data = {}
        for year in range(self.start.year, self.end.year + 1):
            with open(self.path + '/' + str(year) + '.txt') as f:
                print(year)
                all_data.update(json.load(f))
        for date in self._time_range():
            day = str(date).split()[0][0:7]
            if day not in self.changes:
                self.changes.update({day: all_data[day]})


class InflationUA(Inflation):
    """
    Represents UA CPI information
    """

    PATH = 'ratesua'

    def __init__(self):
        super().__init__(self.PATH)


class InflationUS(Inflation):
    """
    Represents US CPI information
    """
    PATH = 'ratesus'

    def __init__(self):
        super().__init__(self.PATH)
