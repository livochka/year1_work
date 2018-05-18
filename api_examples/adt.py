import calendar
from datetime import date
import json
from urllib.request import urlopen
import seaborn as sns
import matplotlib.pyplot as plt


class AvailableCurrencies:
    UAN = 'UAN'
    USD = 'USD'
    RUB = 'RUB'
    EUR = 'EUR'


class UnavailableCurrencyError(Exception):
    pass


class IncorrectDateError(Exception):
    pass


class ExchangeSample:
    """
    Created to represent currency exchange sample
    """

    MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
              '11', '12']

    def __init__(self, currency):
        self._check_currency(currency)
        self.currency = currency
        self.changes = {}
        self.frequency = {}

    @staticmethod
    def _check_currency(currency):
        if currency not in (AvailableCurrencies.UAN, AvailableCurrencies.USD,
                            AvailableCurrencies.RUB, AvailableCurrencies.EUR):
            raise UnavailableCurrencyError

    @staticmethod
    def _check_year(year):
        if  not (2000 <= int(year) <= date.today().year):
            raise IncorrectDateError

    def _source(self, day, month, year, currency):
        raise NotImplementedError

    def month(self, currency2, month, year):
        self._check_currency(currency2)
        self._check_year(year)
        length = calendar.monthrange(int(year), int(month))
        for day in range(length[1] + 1):
            day = str(day) if day > 9 else '0' + str(day)
            self._source(day, month, year, currency2)

    def half_year(self, currency2, year, part=1):
        months = self.MONTHS[0:7] if part == 1 else self.MONTHS[6::]
        for month in months:
            self.month(currency2, month, year)

    def year(self, currency2, year):
        for part in [1, 2]:
            self.half_year(currency2, year, part)

    def _get_frequency(self):
        for key in self.changes:
            rate = round(self.changes[key], 2)
            if rate not in self.frequency:
                self.frequency[rate] = 1
            else:
                self.frequency[rate] += 1

    def most_frequent(self):
        if not self.frequency:
            self._get_frequency()
        return max(self.frequency.keys(), key=(lambda k: self.frequency[k]))

    def middle_value(self):
        values= self.changes.values()
        return sum(values) / len(values)

    def plot_frequency(self):
        if not self.frequency:
            self._get_frequency()
        date = [x[0:3] for x in self.changes.keys()]
        value = self.changes.values()
        plt.plot(date, value)
        plt.show()

    def plot_time(self):
        if self.changes > 31:
            pass





class HryvnaExchange(ExchangeSample):
    def __init__(self):
        super().__init__(AvailableCurrencies.UAN)

    def _source(self, day, month, year, currency):
        url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory' \
              '/exchange?valcode=' + currency + '&date=' + year + month + day + \
              '&json'
        info = urlopen(url).read().decode()

        try:
            info = json.loads(info)[0]
        except IndexError:
            # In case, when this page is not exist
            return None

        self.changes.update({info['exchangedate']: info['rate']})


if __name__ == '__main__':
    my = HryvnaExchange()
    my.year('USD', '2017')
    print(my.changes)
    print(my.most_frequent())
    print(my.plot_frequency())

