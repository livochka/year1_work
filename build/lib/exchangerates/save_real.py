from adt.save_adt import SaveInformationADT
from exchangerates.exchange import HryvnaExRates
from inflation.inflation_information import InflationUS, InflationUA
import json


class SaveRealRateAll(SaveInformationADT):
    """
    Represents data type for saving information about real exchange rates
    """

    def __init__(self):
        super().__init__(None)
        self.nominal = self.initialize(HryvnaExRates()).changes
        self.ua = self.initialize(InflationUA()).changes
        self.us = self.initialize(InflationUS()).changes

    def initialize(self, ifl_dt):
        """
        Initializing by appropriate time
        ifl_dt: nominal exchange data type
        return: initialized instance
        """
        ifl_dt.set_start(2017, 1, 1)
        ifl_dt.set_end(2017, 12, 31)
        ifl_dt.generate()
        return ifl_dt

    def generate(self):
        """
        Generates and saves information for all years
        """
        start_year = '2017'

        for key, val in self.ua.items():
            date = key + '-01'
            if key.startswith(start_year):
                real_rate = self.nominal[date] * val / self.us[key]
                self.changes.update({key: real_rate})
            else:
                self.save('exchangerates/ratesreal/' + start_year + '.txt')
                start_year = str(int(start_year) + 1)
                self.changes = {key: self.nominal[date] * val / self.us[key]}
            self.save('exchangerates/ratesreal/' + start_year + '.txt')
