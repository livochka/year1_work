# Final part with example for each type data

from exchangerates.exchange import HryvnaExRates, RealExchange
import plotly as py
from plotly import tools
from datetime import datetime
from adt.colors import AvailableColors
from inflation.inflation_information import InflationUA, InflationUS


def get_date(tp='start'):
    """
    Getting the date from user
    tp: type of date, for example: start, end
    return: year, month, day
    """
    while True:
        try:
            answer = input('Enter the {} date, please, in form day.month.year: '
                           ''.format(tp))
            day, month, year = list(map(int, answer.split('.')))
            if datetime(2008, 1, 1) <= datetime(year, month, day) < datetime(
                    2018, 1, 1):
                return year, month, day
        except ValueError:
            print('Incorrect format, date must be in ranges 01.01.2008 - '
                  '01.01.2018')
            continue


def generate_information(info_dt, start, end):
    """
    Generating information for particular data type
    info_dt: InformationADT
    start: start date
    end: end date
    return: info_dt with generated information
    """
    year, month, day = start
    year1, month1, day1 = end
    info_dt.set_start(year, month, day)
    info_dt.set_end(year1, month1, day1)
    info_dt.generate()
    return info_dt


def main():

    # Getting the start and the end
    start = get_date()
    end = get_date('end')

    # Generating of information inside of data types
    nominal = generate_information(HryvnaExRates(), start, end)
    real = generate_information(RealExchange(), start, end)
    ua_inflation = generate_information(InflationUA(), start, end)
    us_inflation = generate_information(InflationUS(), start, end)

    # Creating graph objects for each DT
    data_nominal = nominal.plot('Nominal exchange rate', AvailableColors.RED)
    data_real = real.plot('Real exchange rate', AvailableColors.ORANGE)

    data_ua = ua_inflation.plot('CPI in the UA', AvailableColors.BLACK)
    data_us = us_inflation.plot('CPI in the US', AvailableColors.PINK)

    # Creating greed for all graphs
    fig = tools.make_subplots(rows=2, cols=2,
                              subplot_titles=('Exchange rates nominal',
                                              'CPI rates in the UA',
                                              'Exchange rates real',
                                              'CPI rates in the USA'))
    fig.append_trace(data_nominal, 1, 1)
    fig.append_trace(data_real, 2, 1)
    fig.append_trace(data_ua, 1, 2)
    fig.append_trace(data_us, 2, 2)

    py.offline.plot(fig, 'Final_result.html')


if __name__ == '__main__':
    main()
