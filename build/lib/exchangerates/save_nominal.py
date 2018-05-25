# Created to save the information about hryvna exchange rates
# from NBU API


import calendar
import json
from urllib.request import urlopen
from adt.save_adt import SaveInformationADT


class SaveExchangeYear(SaveInformationADT):
    """
    Saving all available information about currency exchange in the
    year
    """

    def __init__(self, year):
        self.cur1 = "UAN"
        self.cur2 = 'USD'
        super().__init__(year)

    def generate(self):
        """
        Generates information about changes in self.cur1 to self.cur2 in
        self.year
        """
        for month in self.MONTHS:

            # Getting for each month

            month_info = {}
            length = calendar.monthrange(self.year, int(month))

            for day in range(1, length[1] + 1):

                # Getting for each day

                day = str(day) if day > 9 else '0' + str(day)
                try:
                    month_info.update(self._source(day, month,
                                                   str(self.year),
                                                   self.cur2))
                except TypeError:
                    continue

            self.changes.update(month_info)

    def _source(self, day, month, year, currency):
        """
        Provides GET-request to NBU to get hryvna exchange rate for date
        day, month, year: date
        currency: currency you want to get hryvna exchange rate for
        """

        url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory' \
              '/exchange?valcode=' + currency + '&date=' + year + month + day + \
              '&json'
        info = urlopen(url).read().decode()

        try:
            info = json.loads(info)[0]
        except IndexError:
            # In case, when this page is not exist
            return None
        date = '-'.join(reversed(info['exchangedate'].split('.')))

        return {date: info['rate']}
