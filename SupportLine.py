import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr

yf.pdr_override() # <overriding yf bug
start =dt.datetime(1980,12,1)  #define start for dataframe
now = dt.datetime.now()   #define end for dataframe
stock=""

stock = input("Enter the stock symbol or type quit: ")
while stock != "quit":          #enter the main loop
  df = pdr.get_data_yahoo(stock, start, now)   # this gets the daily dataframe

  df.drop(df[df["Volume"]<5000].index, inplace=True)  #filtering out all volume with less than 5000 shares a day

  dfmonth=df.groupby(pd.Grouper(freq="M"))["High"].max() #here we are getting the monthly frequency and getting the monthly high column of the pandas dataframe

  slDate=0 # date of the most recent value
  lastSLV=0 # the most recent line of support value
  currentDate="" # current date of the green line value the program will be keeping track of
  curentSLV=0 # current green line value the program will be keeping track of
  for index, value in dfmonth.items():   #prints out all the monthly highs and compares which is the all time high
    if value > curentSLV:        # checking new all time highs
      curentSLV=value    #if correct, set the new value and the current date equal to the index
      currentDate=index
      counter=0
    if value < curentSLV:
      counter=counter+1

      if counter==3 and ((index.month != now.month) or (index.year != now.year)):  # ensuring that 3 months have passed until we can draw the line
          if curentSLV != lastSLV:  #resetting the process and looking for the next support line.
            print(curentSLV)
          slDate=currentDate
          lastSLV=curentSLV
          counter=0

  if lastSLV==0:  # message to be returned if there are no green lines
    message=stock+" has not formed a green line yet"
  else:
    message=("Last Green Line: "+str(lastSLV)+" on "+str(slDate))  #prints the last support line and the date

  print(message)
  stock = input("Enter the stock symbol or type quit : ")
