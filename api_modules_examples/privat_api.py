# Module exist to get info from PrivatBank API

import urllib.request, urllib.parse, urllib.error
import json

url = 'https://api.privatbank.ua/p24api/'


# Exchange course for today: buy and sale


def get_course(operation='buy', currency="USD"):
    """
    Getting information about real exchange course for today: buy or sale
    operation: 'buy' or 'sale'
    currency: currency id, may be: "USD", "EUR", "RUR", "BTC"
    return: exchange course
    """
    ex = urllib.request.urlopen(url + 'pubinfo?json&exchange&coursid=5')
    data = ex.read().decode()
    exchange = [i for i in json.loads(data) if i['ccy'] == currency][0]
    return exchange[operation]


def get_currency_date(date='21.06.2011', currency='USD'):
    """
    Getting of exchange course for any date and any currency
    (str, str) -> tuple
    date: date in form 'dd.mm.yyyy'
    currency: currency id
    return: exchange course (buy rate, sale rate)
    """

    get_date = urllib.request.urlopen(url + 'exchange_rates?json&date=' + date)
    data = get_date.read().decode()

    try:
        data = [i for i in json.loads(data)['exchangeRate']
                if i['currency'] == currency][0]
    except IndexError:
        return 'Information about this date: {}, and this currency: {} - ' \
               'does not exist'.format(date, currency)

    return data["purchaseRate"], data["saleRate"]


if __name__ == '__main__':
    print(get_course(operation='sale', currency='EUR'))
    print(get_currency_date())
    print(get_currency_date('06.11.2005', 'RUR'))
