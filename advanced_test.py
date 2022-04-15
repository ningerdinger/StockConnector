import requests
import os
import pandas as pd

from io import StringIO

def get_eod_data(symbol="AAPL.US", api_token=os.environ['API_EOD'], session=None):
    if session is None:
        session = requests.Session()
        url = 'https://eodhistoricaldata.com/api/eod/%s' # symbol

        params = {"api_token": api_token}

        r = session.get(url, params=params)

        if r.status_code == requests.codes.ok:
            df = pd.read_csv(StringIO(r.text), skipfooter=1, parse_dates=[0], index_col=0, engine='python')
            return df
            
        else:
            raise Exception(r.status_code, r.reason, url)

get_eod_data()