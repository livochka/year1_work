from exchangerates.exchange import HryvnaExRates, RealExchange
import plotly as py
from adt.colors import AvailableColors

# Creating ang generating information about nominal rates
n = HryvnaExRates()
n.set_start(2008, 1, 1)
n.set_end(2017, 12, 31)
n.generate()

# Creating ang generating information about real rates
r = RealExchange()
r.set_start(2008, 1, 1)
r.set_end(2017, 12, 31)
r.generate()

# Plotting data
data_n = n.plot('nominal exchange rate', AvailableColors.RED)
data_r = r.plot('real exchange rate', AvailableColors.ORANGE)
data = [data_n, data_r]
py.offline.plot(data, 'data.html')