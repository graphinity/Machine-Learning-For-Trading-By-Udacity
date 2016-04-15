'''
Created on Apr 6, 2016

@author: karya
'''
from os.path import os

import pandas as pd


def symbol_to_path(symbol, base_dir=""):
    """ Return csv file path given tricker symbol"""
    return os.path.join(base_dir, "{}_Stock_Data.csv".format(str(symbol)))

def get_data(symbols, dates):
    """ Return stock data (Adj close) for given symbols from csv file"""
    df=pd.DataFrame(index=dates)
    if 'Google' not in symbols:  # Add Google for reference, if absent
        symbols.insert(0,'Google')
    
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True, usecols=['Date','Adj Close'],na_values=['nan'])  # read in data
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        df=df.join(df_temp)
        if symbol == 'Google':
            df=df.dropna(subset=["Google"])
    
    return df

def test_run():
    # Define a date range
    dates = pd.date_range('2016-01-15', '2016-01-20')

    # Choose stock symbols to read
    symbols = ['Google', 'Apple']
    
    # Get stock data
    df = get_data(symbols, dates)
    
    # Slice by row range(dates) using DataFrame.ix[] selector
    print(df.ix['2016-01-01':'2016-12-31'])  # Data for one month
    
    # Slice by column (symbols)
    print(df['Google'])
    print(df[['Apple','Google']])
    
    # Slice by row range(dates) using DataFrame.ix[] selector
    print(df.ix['2016-01-01':'2016-12-31',['Apple','Google']])  # Data for one month
    

if __name__ =="__main__":
   test_run()