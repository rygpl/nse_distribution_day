# Load the Pandas libraries with alias 'pd' 
import pandas as pd
import numpy as np 

# Read data from file '^NSEI.csv' downloaded from yahoo
df = pd.read_csv("^NSEI.csv") 

#Define the column names in the file
df.columns = ['Date','Open','High',
                     'Low','Close','Adj Close','Volume']
       
 #current day adjusted close price                    
cacp = df['Adj Close'].fillna(0).astype(float)
 #previous day adjusted close price    
pacp = df['Adj Close'].shift(1).fillna(0).astype(float)
#current trade date
ctd = df['Date']
#previous trade date trade date
ptd = df['Date'].shift(1).fillna(0)
#percentage change in price from previous day
ppc = round(((cacp-pacp)*100/pacp),2)

#current day volume
cv=df['Volume'].fillna(0)
#previous day volume
pv=df['Volume'].shift(1).fillna(0)


#pc = (df['Adj Close'] - df['Adj Close'].shift(1)).fillna(0)

#create a new data frame of required columns
summary = pd.DataFrame(data=dict(s1=ctd,  s2=ptd,s3=cacp.astype(int), s4=pacp.astype(int),s5=ppc.astype(float),s6=cv.astype(int),s7=pv.astype(int)))
summary.columns = ["Current Trading Date","Previous  Trading Date","Current Day Adjusted CLose Price","Previous Day Adjusted Close Price","Percentage Price Change","Current Volume","Previous Volume"]

#check if price has lost more than 0.2 percent
pc1=summary['Percentage Price Change'] <-0.2

#check volume diff
vol_diff = summary['Current Volume'] - summary['Previous Volume'] 

#define summary to be printed
summary['Distribution_Day'] = summary['Percentage Price Change'] <-0.2
summary['vol_diff'] = vol_diff
#print(summary['Percentage Price Change'] <-0.2)

filter = summary["Distribution_Day"]== True


filter.where(filter, inplace = True)

#Distribution day is a day when price has lost more than 0.2 pc with increased volume
newdf = summary.loc[(summary.Distribution_Day == True) & (summary.vol_diff > 0)]

newdf.to_csv("nse_distribution_day.csv", sep=',', header=True)