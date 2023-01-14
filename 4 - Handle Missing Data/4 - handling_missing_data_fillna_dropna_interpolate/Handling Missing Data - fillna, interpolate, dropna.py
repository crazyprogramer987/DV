#  Handling Missing Data - fillna, interpolate, dropna

import pandas as pd

# it will convert day column in date formate
df = pd.read_csv("weather_data.csv",parse_dates=['day'])
type(df.day[0])
print(df)



#set index
print(df.set_index('day',inplace=True))




#   fillna
# Fill all NaN with one specific value

new_df = df.fillna(0)
print(new_df)




#  Fill na using column names and dict

new_df = df.fillna({
        'temperature': 0,
        'windspeed': 0,
        'event': 'No Event'
    })
print(new_df)



#   Use method to determine how to fill na values

# in this NaN upper data fill the NaN value (forward fill)

new_df = df.fillna(method="ffill")
print(new_df)





##  in this NaN lower data fill the NaN value  (backward fill)
new_df = df.fillna(method="bfill")
print(new_df)





#   limit parameter

new_df = df.fillna(method="ffill",limit=1)
print(new_df)



#  interpolate
#give the inbetween values   Linear interpolation
new_df = df.interpolate()
print(new_df)



# guss the value with respectto time
new_df = df.interpolate(method="time") 
print(new_df)




##    dropna

# remove all the row which has NaN value

new_df = df.dropna()
print(new_df)




# remove thos row which have all NaN value

new_df = df.dropna(how='all')
print(new_df)




# if row have 1 NaN value keep the row
new_df = df.dropna(thresh=1)
print(new_df)




# Inserting Missing Dates

dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df.reindex(idx)



































