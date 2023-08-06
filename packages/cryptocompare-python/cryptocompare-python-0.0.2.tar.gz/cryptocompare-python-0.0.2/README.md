# cryptocompare-Python-API

[![CodeQL](https://github.com/Alejandro193/CryptoCurrency/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/codeql-analysis.yml)
[![Upload Python Package](https://github.com/Alejandro193/CryptoCurrency/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Ventura94/NOWPayments-Python-API/actions/workflows/python-publish.yml)

A Python wrapper for the [Cryptocompare API](https://min-api.cryptocompare.com/documentation). 

The api call descriptions are from the official documentation.

## Getting Started
To get your API Key visit [Cryptocompare Web Site](https://www.cryptocompare.com/cryptopian/api-keys) but is not implemented yet in this package


To install the wrapper, enter the following into the terminal.
```bash
pip install cryptocompare-python
```

API Key is optional here
```python
from cryptocompare-py import CryptoCurrency
currency = CryptoCurrency()

simple_exchange_rate = currency.get_single_exchange_rate('BTC','USD')
print(simple_exchange_rate)

multiple_exchange_rate = currency.get_multiple_exchange_rate('BTC','USD','EUR','CAD')
print(multiple_exchange_rate)
```