'''
Created on Apr 6, 2016

@author: karya
'''
import pandas as pd

def test_run():
    df = pd.read_csv("Google_Stock_Data.csv")
    # print(df)
    # print(df.head())
    # print(df.tail())
    # print(df.tail(3))
    print(df[10:21])

if __name__ =="__main__":
   test_run()