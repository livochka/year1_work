# Created to test the InflationUA and the InflationUS classes

from inflation.inflation_information import InflationUA, InflationUS
import plotly as py
from adt.colors import AvailableColors

# Preparing UA CPI data
ukraine = InflationUA()
ukraine.set_start(2014, 1, 1)
ukraine.set_end(2017, 1, 1)
ukraine.generate()

# Preparing the US CPI

united_states = InflationUS()
united_states.set_start(2014, 1, 1)
united_states.set_end(2017, 1, 1)

united_states.generate()
uk_data = ukraine.plot('CPI in the UA', AvailableColors.RED)
us_data = united_states.plot('CPI in the US', AvailableColors.ORANGE)
data = [uk_data, us_data]
py.offline.plot(data, 'data.html')

