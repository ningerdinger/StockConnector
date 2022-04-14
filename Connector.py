'''
The source is from

https://eodhistoricaldata.com/financial-apis/?roistat=google1_g_128816179848_534670027147_stock%20api&roistat_referrer=&roistat_pos=&utm_source=google_search&utm_medium=cpc&utm_campaign=EXT_Europe&roistat_referrer=&roistat_pos=&roistat=google1_g_128816179848_534670027147_stock%20api&gclid=Cj0KCQjwjN-SBhCkARIsACsrBz493ul8kflB6ZqeaFZxXAiZevSw09KWVnj2Ly-6ZiOvu-FQ_1ypFPIaAgPkEALw_wcB
'''

import os
from eod import EodHistoricalData
from random import randint




class Connector:

    def __init__(self, url):
        self.url = url
        # load the key from the enviroment variables
        api_key = os.environ['API_EOD']

        # Create the instance 
        client = EodHistoricalData(api_key)
        # predefine some instruments
        symbol='AAPL.US'
        goverment_bond = 'SW10Y.GBOND'
        corporate_bond = 'US00213MAS35.BOND'

        # Quick usage
        # weekly prices for the Swiss goverment bond
        stock_prices = client.get_prices_eod(goverment_bond, period='w', order='a')
        # Short interest
        get_short_interest = client.get_short_interest(symbol, to='2021-07-04')
        # Fundamental data for the stock
        resp = client.get_fundamental_equity(symbol, filter_='Financials::Balance_Sheet::quarterly') # Stock - check

