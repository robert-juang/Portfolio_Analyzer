import yfinance as yahooFinance
import pandas as pd
import datetime 

#define start and end year for our data 
START_YEAR = 2013 
END_YEAR = 2022

#can be changed
STOCK_STRING = "NDX	ATVI	ADBE	AMD	ALXN	ALGN	GOOGL	GOOG	AMZN	AMGN	ADI	ANSS	AAPL	AMAT	ASML	ADSK	ADP	BIDU	BIIB	BMRN	BKNG	AVGO	CDNS	CDW	CERN	CHTR	CHKP	CTAS	CSCO	CTXS	CTSH	CMCSA	CPRT	COST	CSX	DXCM	DOCU	DLTR	EBAY	EA	EXC	EXPE	FB	FAST	FISV	GILD	IDXX	ILMN	INCY	INTC	INTU	ISRG	JD	KLAC	KHC	LRCX	LBTYA	LBTYK	LULU	MAR	MXIM	MELI	MCHP	MU	MSFT	MRNA	MDLZ	MNST	NTES	NFLX	NVDA	NXPI	ORLY	PCAR	PAYX	PYPL	PEP	PDD	QCOM	REGN	ROST	SGEN	SIRI	SWKS	SPLK	SBUX	SNPS	TMUS	TTWO	TSLA	TXN	TCOM	ULTA	VRSN	VRSK	VRTX	WBA	WDAY	WDC	XEL	XLNX"
STOCK_LIST = STOCK_STRING.split("\t")

def getDataAndStore(): 
    GetFacebookInformation = yahooFinance.Ticker("META")
    START_DATE = datetime.datetime(START_YEAR, 1, 1)
    END_DATE = datetime.datetime(END_YEAR+1,1,1)

    #preprocess the dates 
    df=GetFacebookInformation.history(start=START_DATE,end=END_DATE) 
    temp = df.index.tolist() 
    date = []
    for i in range(len(temp)): 
        date.append(str(temp[i])[:10])
    output = pd.DataFrame(index=date)

    for index, ticker in enumerate(STOCK_LIST): 
        GetTickerInformation = yahooFinance.Ticker(ticker)
        df = GetTickerInformation.history(start=START_DATE, 
                                        end=END_DATE)
        #drop everything except Close and filter data
        output[ticker] = df["Close"]
        print(f"Request: {index} Finished Processing, {ticker}")

    #drop data which are not retrieved (could be due to variety of reason) 
    output.dropna(axis=1, how='any', inplace=True)
    output.to_csv("nasdaq_data.csv")

    print("Data Created") 

    #output the data in folders
    DATE_YEARS = [i for i in range(START_YEAR, END_YEAR+1)] 

    a = pd.read_csv("nasdaq_data.csv")

    for years in DATE_YEARS: 
        b = a[a["Date"].apply(lambda x: x[-2:] == str(years)[-2:])]
        b.to_csv(f"./nasdaq_data/nasdaq{years}.csv")
        print(f"Converted {years} nasdaq data")
    
    print("Stored data in nasdaq_data")

getDataAndStore() 
 