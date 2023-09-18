# EDITED Starter code for Homework 4

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
filepath = os.path.join('/Users/NStrom_School/Desktop/HAS_Tools/forecasting/data', filename)
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

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

print(type(flow_data))
(type(flow_data[:,3]))
## 4	Forecast due 9/18/23	
# 9/16/23 - last date can use	
# 1 wk out: 9/17/23	- 9/23/23	
# 2 wk out: 9/24/23	- 9/30/23		
# %%
# 1 wk out: 9/17/23	- 9/23/23	

Sept_17_23 = (flow_data[:,3] > 50) & (flow_data[:,3] <= 350) & (flow_data[:,1]==9) & (flow_data[:,2] >= 17) & (flow_data[:,2] <= 23)
flow_count = np.sum(Sept_17_23)
criteria1 = Sept_17_23
pick_data = flow_data[criteria1, 3]
flow_mean = np.mean(pick_data)

print(flow_count)
print(flow_mean)
# calculates the mean for the data range of 9/17/23- 9/23/23 through all septembers between flow of 50 and 350 

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "between Sept 17-23 from 1989 until 2022")

# %%
# 2 wk out: 9/24/23	- 9/30/23		
Sept_24_30 = (flow_data[:,3] > 50) & (flow_data[:,3] < 350) & (flow_data[:,1]==9) & (flow_data[:,2] >= 23) & (flow_data[:,2] <= 30)
flow_count2 = np.sum(Sept_24_30)
criteria2 = Sept_24_30
pick_data = flow_data[criteria2, 3]
flow_mean2 = np.mean(pick_data)

print(flow_count2)
print(flow_mean2)
# calculates the mean for the data range of 9/23/23	- 9/30/23 through all septembers between flow of 50 and 350 

print("Flow meets this critera", flow_count2, " times")
print('And has an average value of', flow_mean2, "between Sept 24-30 from 1989 until 2022")


# %%


mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[criteria1, 3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(flow_data[criteria1, 3], q=[0,0.01, 0.05, 0.01])
print('Histogram plot of flow values from Sept 17-23')


plt.hist(flow_data[criteria2, 3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')


# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants2 = np.quantile(flow_data[criteria2, 3], q=[0,0.01, 0.05, 0.01])
print('Histogram plot of flow values from Sept 24-30')


# Or computing on a colum by column basis 
# flow_quants2 = np.quantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
# print('Method two flow quantiles:', flow_quants2[:,3])

# %%
flow_mean = np.mean(flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')


# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.quantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column


## ignore this junk below 


# %%
print(np.shape(flow_data))
print(type((flow_data[:1])))

# %%
## times greater than in Sept than 1wkout: 126... 456
## times greater in Sept than 2wkout 118... 511
Sept = (flow_data[:,3] > 118) & (flow_data[:,1]==9)
flow_count = np.sum(Sept)

criteria1 = Sept
pick_data = flow_data[criteria1, 3]
flow_mean = np.mean(pick_data)

print(flow_count)
# %%


# %%
year = 2010
b = np.sum((flow_data[:,0] > year),(flow_data[:,1]==9))

flow_count_sept = np.sum(b)
print(flow_count_sept)

c = np.sum((flow_data[:,3] > 126) & (flow_data[:,1]==9) & (flow_data[:,0] <= year))
print(c)

d = np.sum((flow_data[:,3] > 118) & (flow_data[:,1]==9) & (flow_data[:,0] <= year))
print(d)




# %%
Sept_17_23 = (flow_data[:,3] > 50) & (flow_data[:,3] <= 350) & (flow_data[:,1]==9) & (flow_data[:,2] >= 17) & (flow_data[:,2] <= 23)
flow_count = np.sum(Sept_17_23)
criteria1 = Sept_17_23
pick_data = flow_data[criteria1, 3]
flow_mean = np.mean(pick_data)

print(flow_count)
print(flow_mean)

# %%
