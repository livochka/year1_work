# Module created to get information from National Bank of Ukraine

import urllib.request, urllib.parse, urllib.error
import json

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/inflation?period=m' \
      '&date='


# Getting consumer price index (CPI) for 2013 and 2015 years in Lvivska obl


def get_cpi_Ukraine(date, ku='13'):
    '''
    (str, str) -> tuple
    date: date, in form 'YYYYMM'
    ku: index of region ('13' for Lvivska obl)
    return: CPI for the date and the region
    '''

    ex_1 = urllib.request.urlopen(url + date + '&json')

    data_1 = ex_1.read().decode()
    year_data = json.loads(data_1)

    # Adding of info with value 'Total' on key 'mcrd081'
    # what means that this is CPI and value '13' on key 'ku'
    # what means that this is about Lvivska oblast

    for x in year_data:
        if x['mcrd081'] == 'Total' and x['ku'] == ku and x['tzep'] == 'DTPY_':
            return x['dt'], x['value']


if __name__ == '__main__':
    print(get_cpi_Ukraine('201602'))

    # Information about Vinnitsa in the same month
    print(get_cpi_Ukraine('201602', '1'))
