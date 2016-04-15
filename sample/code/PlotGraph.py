'''
Created on Apr 6, 2016

@author: karya
'''
import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    """ Draw graph for Adj Close 
    """      
    df = pd.read_csv("Google_Stock_Data.csv")  # read in data
    print(df[['Adj Close','High']].plot())
    plt.show()
        
if __name__ =="__main__":
   test_run()
    