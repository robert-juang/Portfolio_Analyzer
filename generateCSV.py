#Note: Combine with getData.py. It's just that I already have the data and don't want to run the script again 

import yfinance as yahooFinance
import pandas as pd
import datetime 

START_YEAR = 2013 
END_YEAR = 2022

DATE_YEARS = [i for i in range(START_YEAR, END_YEAR+1)] 

a = pd.read_csv("nasdaq_data.csv")

for years in DATE_YEARS: 
    b = a[a["Date"].apply(lambda x: x[-2:] == str(years)[-2:])]
    b.to_csv(f"./nasdaq_data/nasdaq{years}.csv")
    print(f"Converted {years} nasdaq data")
    
print("Done")