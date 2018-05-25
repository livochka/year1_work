import json
import urllib.request as rq
import pandas as pd
from adt.save_adt import SaveInformationADT


class SaveInflationUA(SaveInformationADT):
    """
    Created to save cpi UA data
    """

    def __init__(self, year, region):
        super().__init__(year, region)

    def generate(self):
        """
        Getting CPI values for particular year
        """
        for month in self.MONTHS:
            try:
                self.changes.update(self._source(month))
            except (json.decoder.JSONDecodeError, TypeError):
                print('This value is not accessible')
                break

    def _source(self, month):
        """
        Processing GET-request to NBU API
        month: parameter of date
        return: dictionary with date as key, the CPI as value
        """

        url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/' \
              'inflation?period=m&date='
        data = rq.urlopen(url + str(self.year) + month + '&json')
        data = json.loads(data.read().decode())
        key = str(self.year) + '-' + month
        for x in data:
            if x['mcrd081'] == 'Total' and x['ku'] == self.region and \
                            x['tzep'] == 'DTPY_':
                return {key: x['value']}


class SaveAllInflationUS(SaveInformationADT):
    """
    Created to save information about CPI in the US
    """

    def __init__(self):
        super().__init__(None)

    def generate(self):
        """
        Getting appropriate information from .xlsx file
        """
        data = {}
        all_data = pd.read_excel('ratesus/us.xlsx')
        data_keys = all_data['DATE']
        data_values = all_data['RATE']
        for ind in range(len(data_values)):
            month = '0' + str(data_keys[ind].month) \
                if data_keys[ind].month < 10 else str(data_keys[ind].month)
            date = str(data_keys[ind].year) + '-' + month
            data.update({date: data_values[ind]})
        self.parse_dictionary(data)

    def parse_dictionary(self, data):
        """
        Saving all information to files with the appropriate year
        data: dictionary, date is key, cpi is value
        """
        year = '2008'
        current = {}
        for date in data:
            if date.startswith(year):
                current.update({date[0:7]: data[date]})
            else:
                self.changes = current
                self.save('ratesus/' + year + '.txt')
                current, year = {date[0:7]: data[date]}, str(int(year) + 1)
