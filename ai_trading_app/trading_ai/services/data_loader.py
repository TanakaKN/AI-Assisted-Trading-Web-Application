import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance.
    """
    df = yf.download(ticker, start=start_date, end=end_date)
    df.dropna(inplace=True)
    return df
