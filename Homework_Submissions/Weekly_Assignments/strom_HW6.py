# Starter code for week 6 Pandas

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
filepath = os.path.join('/Users/NStrom_School/Desktop/HAS_Tools/Week 6', 'streamflow_week6.txt')
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)


# wk 1 -- start:10/8/23, end:10/14/23 
# wk 2 -- start:10/15/23, end:10/21/23

# %% 

## finding WEEK 1 -- strt 10/08 - 10/14

#%%
SepOct_flowrange = data[((data["month"] == 9) & (data["day"] > 25)) | ((data["month"] == 10) & (data["day"] >= 1) & (data["day"] <= 6))]
    # selecting the values from Sept and Oct within the past 2 week time frame
data_2023 = SepOct_flowrange[SepOct_flowrange['year'] == 2023]

#%%
SepOct_flowrange_MEAN = SepOct_flowrange.groupby(['year'])[['flow']].mean().reset_index()

SepOct_flowrange_MEAN
#%%
data_2023
avg_2023 = data_2023['flow'].mean()
avg_2023

# %% 
similar_flow = SepOct_flowrange_MEAN[(SepOct_flowrange_MEAN['flow'] > .6*avg_2023) & (SepOct_flowrange_MEAN['flow'] < 1.4*avg_2023)]

similar_flow['year']

#%% 
# wk 1 -- start:10/8/23, end:10/14/23 

## finding average of similar years according to the past two weeks from the list of years


# Key_data = Oct_08_thru_14[(Oct_08_thru_14['year'] == similar_flow['year'])]

Oct_08_thru_14 = data[(data["month"] == 10) & (data["day"] >= 8) & (data["day"] <= 14) & ((data["year"] == 2000) | (data["year"] == 2003) | (data["year"] == 2005) | (data["year"] == 2006) | (data["year"] == 2008) | (data["year"] == 2009) | (data["year"] == 2012) | (data["year"] == 20017) | (data["year"] == 2020) | (data["year"] == 2023))] 

#%% Prediction for 1 week out 
One_week_out_prediction = Oct_08_thru_14['flow'].mean()
One_week_out_prediction = round(One_week_out_prediction, 3)


#%% Two weeks out Prediction -- start:10/15/23, end:10/21/23

Oct_15_thru_21 = data[(data["month"] == 10) & (data["day"] >= 15) & (data["day"] <= 21) & ((data["year"] == 2000) | (data["year"] == 2003) | (data["year"] == 2005) | (data["year"] == 2006) | (data["year"] == 2008) | (data["year"] == 2009) | (data["year"] == 2012) | (data["year"] == 20017) | (data["year"] == 2020) | (data["year"] == 2023))] 

Two_week_out_prediction = Oct_15_thru_21['flow'].mean()
Two_week_out_prediction = round(Two_week_out_prediction, 3)


#%% 

print('One week out prediction (10/08-14):', One_week_out_prediction,'cfs')
print('Two weeks out prediction (10/15-21):', Two_week_out_prediction,'cfs')



# %% ____________________________________________________________________________________________________________



#%% (1) Provide a summary of the data frames properties.

data.info()
data.describe()
# What are the column names?
data.columns
    ## ['agency_cd', 'site_no', 'datetime', 'flow', 'code', 'year', 'month', 'day']
# What is its index? -- index is the names for the columns in form of Pandas DF

# What data types do each of the columns have?
data.dtypes
# site_no        int64
# datetime      object
# flow         float64
# code          object
# year           int64
# month          int64
# day            int64

#%% (2) Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.

flow = data['flow']
flow.describe()

#%% (3) Provide the same information but on a monthly basis (i.e. for all January, February, March etc). (Note: you should be able to do this with one or two lines of code)
flow_by_month = data.groupby(['month'])[['flow']].describe()
flow_by_month

#%% (4) Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month and flow values in your summary. (Hint: you will want to use the sort_values function for this)
Five_lowest_flow_values = data.sort_values(by="flow", ascending=True).iloc[0:5,:]

Five_lowest_flow_values
#%%
DL = len(data)
Five_highest_flow_values = data.sort_values(by="flow", ascending=False).iloc[0:5,:]
Five_highest_flow_values
#%% (5) Provide a list of historical dates with flows that are within 10% of your week 1 forecast value for the month of September. If there are none than increase the %10 window until you have at least one other value and report the date and the new window you used
# Week 1 September forecast value predictions 
    ## 95.5 -- 1 week out 
    ## 105.4 -- 2 week out 
# calc the avg of my two week predictions to a get a single week 1 Sept prediction
a = [95.5, 105.4]
print(a)
s1p = np.average(a)

print(s1p)

s10p = s1p * 1.10
s10m = s1p * .90
print(s10m)
# %% 
print('The following values are between', s10m, 'and', s10p,', which are the historical September flow values within 10 percent of the week 1 prediction')
values_win_10p = data[(data["flow"] > s10m) & (data["flow"] < s10p)]

values_win_10p['flow'].max()

# avg_monthly_precip[(avg_monthly_precip["precip_in"] < 2) & (avg_monthly_precip["precip_in"] > 1)]

values_win_10p





# %% ____________________________________________________________________________________________________________

# %%
# Warm up exercises: 
data 
# %%
# 1. How do you see a quick summary of what is in `data`?
data.info()
data.describe()

# %%
# 2. How do you get a listing of the columns in `data`?
data.columns

# %%
# 3. How do you select the streamflow column in `data`?
data['flow']

#%%
# 5. How do you get the last streamflow value from `data`?
data.iloc[-1,3] ## returns data from Friday 10/06/23 = 72.4
#%%
# 6. What is the mean streamflow value for entire period?
mean_flow_all_time = data['flow']

mean_flow_all_time.mean() ## = 352.511
#%%
# 7. What is the maximum value for the entire period?

mean_flow_all_time.max() ## = 63400.0

#%%
# 8. How do you find the maximum streamflow value for each year?
a = data.groupby(['year'])[['flow']]

a.max()