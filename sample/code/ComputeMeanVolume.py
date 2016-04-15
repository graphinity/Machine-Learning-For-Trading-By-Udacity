'''
Created on Apr 6, 2016

@author: karya
'''
import pandas as pd

def get_max_close(symbol):
    """ Get Max closing price for the day
    """      
    df = pd.read_csv("{}_Stock_Data.csv".format(symbol))  # read in data
    return df["Volume"].mean()

def test_run():
    """ Function called by Test Run.
    """
    for symbol in ['Apple', 'Google']:
        print("Max Close")
        print(symbol, get_max_close(symbol))
        
if __name__ =="__main__":
   test_run()
    