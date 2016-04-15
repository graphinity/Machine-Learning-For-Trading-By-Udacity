'''
Created on Apr 6, 2016

@author: karya
'''
import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.pytables import IndexCol


def test_run():
    
   # Define date range
   start_date='2016-01-15'
   end_date='2016-01-20'
   dates=pd.date_range(start_date,end_date)
   # print(dates[0])
   
   # Create an empty dataframe
   df1=pd.DataFrame(index=dates)
   
   # Read SPY data into empty dataframe
   dfspy=pd.read_csv("SPY_HistoricalNav.csv", index_col="Date", parse_dates=True, usecols=['Date','Nav'],na_values=['nan'])
   # print(dfspy)
   
   # Join two dataframes using Dataframe.Join()
   df1=df1.join(dfspy,how='inner')
   print(df1)
   
   # Drop NaN values
   df1=df1.dropna()
   # print(df1)

   # Read in more stocks
   symbols = ['Apple','Google']
   for symbol in symbols:
       df_temp = pd.read_csv("{}_Stock_Data.csv".format(symbol), index_col="Date", parse_dates=True, usecols=['Date','Adj Close'],na_values=['nan'])  # read in data
       # Rename to prevent clash
       df_temp=df_temp.rename(columns={"Adj Close":symbol})
       df1=df1.join(df_temp) # use default = 'left'
   print(df1)

if __name__ =="__main__":
   test_run()