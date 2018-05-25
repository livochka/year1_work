from distutils.core import setup

setup(name='Exchange_rates',
      version='1.0',
      packages=['adt', 'docs', 'exchangerates', 'inflation'],
      py_modules=['exchange_and_inflation', 'cpi_example',
                  'exchange_example', 'exchange_rates_distribution'],
      scripts=['exchange_and_inflation.py'])

