import json
from adt.info_dt import InformationADT


class HryvnaExRates(InformationADT):
    """
    Represent information about exchange rate changes during time period
    """

    def generate(self):
        """
        Reading the information about hryvna exchange rates from the file
        """
        all_data = {}
        for year in range(self.start.year, self.end.year + 1):
            with open('exchangerates/rates/' + str(year) + '.txt') as f:
                all_data.update(json.load(f))
        for date in self._time_range():
            dat = str(date).split()[0]
            self.changes.update({dat: all_data[dat]})
