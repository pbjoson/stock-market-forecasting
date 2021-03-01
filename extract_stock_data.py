# Description ----------------------------------------------------------------------------------------------------------
# The purpose of this script is to extract stock market data via API calls
# We will be working with polygon.io which provides a Free service
# The Free service allows for 5 API calls / minute, end of day data and 2 years of historical data

# Import Libraries -----------------------------------------------------------------------------------------------------
import pandas as pd
import requests

# Functions ------------------------------------------------------------------------------------------------------------


def extract_ticker_data(ticker, date_start, date_end, api_key):
    polygon_api = 'https://api.polygon.io/v2/aggs/ticker/'
    url = polygon_api + ticker + '/range/1/day/' + date_start + '/' + date_end + '?apiKey=' + api_key

    response = requests.get(url)
    return response


# Extract Data ---------------------------------------------------------------------------------------------------------
# First, we must define which tickers we want to track
# We will chose $TSLA, $GME and $AAPL
gme_response = extract_ticker_data('GME', '2021-01-22', '2021-02-28', 'i7Zyh1Lx8fFzgChAeARrcB4YhSCNOVCs')
