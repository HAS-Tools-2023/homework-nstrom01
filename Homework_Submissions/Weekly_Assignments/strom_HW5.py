## WEEk 5 ASSIGNMENT: NUMPY & LOOPS
# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('/Users/NStrom_School/Desktop/HAS_Tools/forecasting/data', 'streamflow_week4.txt')
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )


#%% (1) creating flow_data
# Expand the dates to year month day

data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

#%% (2) Creating flow_5yr
# print(flow_data[flow_data[:,0] >= 2015])

flow_5yr = flow_data[(flow_data[:,0] >= 2015) & (flow_data[:,0] <= 2019)]
flow_5yr = flow_5yr.astype(int)
print(flow_5yr)


#%% printing dimensions
print(flow_5yr.shape)
Five_yr_FlowMean = np.mean(flow_5yr[:,3])
print(Five_yr_FlowMean)

#%% Running statistical checks because the mean flow and the max value shown is a bit surprising in how large it is 
print(Five_yr_FlowMean)
print(np.max(flow_5yr[:,3]))
print(np.min(flow_5yr[:,3]))
print(np.std(flow_5yr[:,3]))
a = np.sum(flow_5yr[:,3])
b = np.size(flow_5yr[:,3])
print(a/b)

#%% (3) Converting daily avg flow from cfs to cubic feet - w/o using loop
SecDay = 86400 # 86400 seconds in a day. 86400 x avg cfs of the day = daily flow
Daily_flow2 = flow_5yr[:,3]
print(Daily_flow2 * SecDay)


#%% (3) Converting daily avg flow from cfs to cubic feet - USING LOOP

Daily_Flow = np.array([i * SecDay for i in flow_5yr[:,3]])
# print(Daily_Flow)
Daily_Flow = (Daily_Flow.reshape(len(Daily_Flow),1))
print(Daily_Flow)

print('the first five daily flow values in 2015 are:',Daily_Flow[0:5,:])

print(np.sum(Daily_Flow))


#%% (4) Creating a time series of monthyl avg flow from the daily flow values
        # 60 months long total
        # 3 columns: [year,month,flow]... 60 rows

flow_monthly = (np.zeros((60,3))).astype(int)
# print(flow_monthly)
flow_monthly[:,0] = np.repeat(np.arange(2015,2020),12)

columns = np.size(flow_monthly[:,0])

month_sets = int(columns / 12)

flow_monthly[:,1] = np.tile(np.arange(1,13),month_sets)
print(flow_monthly)

#%% entering the daily avg flows into the flow_monthly array

for i in range(columns):
    y = flow_monthly[i,0]
    m = flow_monthly[i,1]
    # print(y,m)
    ilist=(flow_5yr[:,0]== y) & (flow_5yr[:,1]== m)
    flow_monthly[i,2] = np.mean(flow_5yr[ilist,3]) # this sets a calculation of a mean sequence interval from the flow_5yr array of colum 4 (pyth column 3)
    # to be within the conditions set of y and m above. It restricts the data chunk that is averaged to the corresponding month. We could not use a set number 
    # for the sequence interval because the size of each month can vary. 
print(flow_monthly)












#%%
# Experimental / tester code
# a = np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
# b = np.zeros((3,4))
# print(a)
# print(b)
# print(a[0,:])









    



















# %%
