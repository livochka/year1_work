import json
from adt.info_dt import InformationADT


class HryvnaExRates(InformationADT):
    """
    Represent an information about nominal exchange rate
    """

    def __init__(self):
        super().__init__()
        self.path = 'exchangerates/rates/'

    def generate(self):
        """
        Reading the information about hryvna exchange rates from the file
        """
        all_data = {}
        for year in range(self.start.year, self.end.year + 1):
            with open(self.path + str(year) + '.txt') as f:
                all_data.update(json.load(f))
        for date in self._time_range():
            dat = str(date).split()[0]
            self.changes.update({dat: all_data[dat]})


class RealExchange(InformationADT):
    """
    Represent an information about real exchange rate
    """

    def __init__(self):
        super().__init__()
        self.path = 'exchangerates/ratesreal/'

    def generate(self):
        """
        Reading the information about hryvna exchange rates from the file
        """
        all_data = {}
        for year in range(self.start.year, self.end.year + 1):
            with open(self.path + str(year) + '.txt') as f:
                all_data.update(json.load(f))
        print(all_data)
        for date in self._time_range():
            dat = str(date).split()[0][0:7]
            self.changes.update({dat: all_data[dat]})
