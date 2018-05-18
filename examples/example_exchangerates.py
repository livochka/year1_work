# Created to test the HryvnaExRates class

from exchangerates.exchange import HryvnaExRates

new = HryvnaExRates()

# Setting the start and the end
new.set_start(2017, 1, 1)
new.set_end(2017, 12, 31)

# Generating of the information
new.generate()

# Plotting the graph
new.plot()

# Plotting the histogram
new.histogram()