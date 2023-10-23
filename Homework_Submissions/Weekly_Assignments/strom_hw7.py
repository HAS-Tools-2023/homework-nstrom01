


#%% 


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


plt.style.use('dark_background')


#%%

## Import the flow data to use
#data = pd.read_table("Wk8_Verde_Data.txt",  sep='\t', skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'])
#data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
#data['year'] = data['year'].astype(int)
#data['month'] = data['month'].astype(int)
#data['day'] = data['day'].astype(int)


#%%

# Set the file name and path to where you have stored the data
filename = 'Wk8_Verde_Data.txt'
filepath = os.path.join('/Users/NStrom_School/Desktop/HAS_Tools/homework-nstrom01/Homework_Working', 'Wk8_Verde_Data.txt')
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



# %%

# %%

# %%

## Compiling historical data from 10/01-10/14
#%% selecting historical data of October 1 thru 14 -> used as references / selection for years to average from
Oct_1thru14_flow = data[(data["month"] == 10) & (data["day"] <= 14) & (data["year"] < 2023)] 

Oct_1thru14_2023_flow = data[(data["month"] == 10) & (data["day"] <= 14) & (data["year"] == 2023)] 
#%% 
Oct_historic_AVG = Oct_1thru14_flow.groupby(['year'])[['flow']].mean().reset_index()

Oct_2023_AVG = Oct_1thru14_2023_flow['flow'].mean()

#%%
Range_A = .10
A_flow_avg = Oct_historic_AVG[(Oct_historic_AVG['flow'] > ((1- Range_A)*Oct_2023_AVG)) & (Oct_historic_AVG['flow'] < ((1+Range_A)*Oct_2023_AVG))]

Range_B = .15
B_flow_avg = Oct_historic_AVG[(Oct_historic_AVG['flow'] > ((1- Range_B)*Oct_2023_AVG)) & (Oct_historic_AVG['flow'] < ((1+Range_B)*Oct_2023_AVG))]

Range_C = .20
C_flow_avg = Oct_historic_AVG[(Oct_historic_AVG['flow'] > ((1- Range_C)*Oct_2023_AVG)) & (Oct_historic_AVG['flow'] < ((1+Range_C)*Oct_2023_AVG))]

Range_D = .30
D_flow_avg = Oct_historic_AVG[(Oct_historic_AVG['flow'] > ((1- Range_D)*Oct_2023_AVG)) & (Oct_historic_AVG['flow'] < ((1+Range_D)*Oct_2023_AVG))]

Range_E = .35
E_flow_avg = Oct_historic_AVG[(Oct_historic_AVG['flow'] > ((1- Range_E)*Oct_2023_AVG)) & (Oct_historic_AVG['flow'] < ((1+Range_E)*Oct_2023_AVG))]

Range_F = .40
F_flow_avg = Oct_historic_AVG[(Oct_historic_AVG['flow'] > ((1- Range_F)*Oct_2023_AVG)) & (Oct_historic_AVG['flow'] < ((1+Range_F)*Oct_2023_AVG))]

Range_G = .50
G_flow_avg = Oct_historic_AVG[(Oct_historic_AVG['flow'] > ((1- Range_G)*Oct_2023_AVG)) & (Oct_historic_AVG['flow'] < ((1+Range_G)*Oct_2023_AVG))]


# %%
B_flow_avg
C_flow_avg


# %%
D_flow_avg
years_of_int_D = D_flow_avg['year'].tolist()
D_15thru21_Flow_List = data[(data['month'] == 10) & 
                      (data['day'] >= 15) & 
                      (data['day'] <= 21) & 
                      (data['year'].isin(years_of_int_D))] # historical avgs of Oct 15 - 21

D_15thru21_YEARLY_AVG = D_15thru21_Flow_List.groupby(['year'])[['flow']].mean().reset_index()

D_Oct15thru10_AVG = round(D_15thru21_YEARLY_AVG['flow'].mean(),3)

print('his avg flow: October 15 - 21: prev 2 weeks w/in .30 of 2023 past 2 weeks average:')
print(D_Oct15thru10_AVG)
print("this flow is between", round((1-Range_D)*Oct_2023_AVG,3) , "and", round((1+Range_D)*Oct_2023_AVG,3))
D_15thru21_SDev = round(D_15thru21_YEARLY_AVG['flow'].std(), 3)
print('std deviation =', D_15thru21_SDev)


#%% 
E_flow_avg
years_of_int_E = E_flow_avg['year'].tolist()
E_15thru21_Flow_List = data[(data['month'] == 10) & 
                      (data['day'] >= 15) & 
                      (data['day'] <= 21) & 
                      (data['year'].isin(years_of_int_E))] # historical avgs of Oct 15 - 21

E_15thru21_YEARLY_AVG = E_15thru21_Flow_List.groupby(['year'])[['flow']].mean().reset_index()

E_15thru21_AVG = round(E_15thru21_YEARLY_AVG['flow'].mean(),3)

print('this avg flow: October 15 - 21: prev 2 weeks w/in .35 of 2023 past 2 weeks average:')
print(E_15thru21_AVG)
print("this flow is between", round((1-Range_E)*Oct_2023_AVG,3) , "and", round((1+Range_E)*Oct_2023_AVG,3))
E_15thru21_SDev = round(E_15thru21_YEARLY_AVG['flow'].std(), 3)
print('std deviation =', E_15thru21_SDev)


#%%
F_flow_avg
years_of_int_F = F_flow_avg['year'].tolist()
F_15thru21_Flow_List = data[(data['month'] == 10) & 
                      (data['day'] >= 15) & 
                      (data['day'] <= 21) &
                      (data['year'].isin(years_of_int_F))] # historical avgs of Oct 15 - 21

F_15thru21_YEARLY_AVG = F_15thru21_Flow_List.groupby(['year'])[['flow']].mean().reset_index()

F_15thru21_AVG = round(F_15thru21_YEARLY_AVG['flow'].mean(),3)

print('this avg flow: October 15 - 21: prev 2 weeks w/in .35 of 2023 past 2 weeks average:')
print(F_15thru21_AVG)
print("this flow is between", round((1-Range_F)*Oct_2023_AVG,3) , "and", round((1+Range_F)*Oct_2023_AVG,3))
F_15thru21_SDev = round(F_15thru21_YEARLY_AVG['flow'].std(), 3)
print('std deviation =', F_15thru21_SDev)

#%%
G_flow_avg
years_of_int_G = G_flow_avg['year'].tolist()
G_15thru21_Flow_List = data[(data['month'] == 10) & 
                      (data['day'] >= 15) & 
                      (data['day'] <= 21) & 
                      (data['year'].isin(years_of_int_G))] # historical avgs of Oct 15 - 21

G_15thru21_YEARLY_AVG = G_15thru21_Flow_List.groupby(['year'])[['flow']].mean().reset_index()

G_15thru21_AVG = round(G_15thru21_YEARLY_AVG['flow'].mean(),3)

print('this avg flow: October 15 - 21: prev 2 weeks w/in .35 of 2023 past 2 weeks average:')
print(G_15thru21_AVG)
print("this flow is between", round((1-Range_F)*Oct_2023_AVG,3) , "and", round((1+Range_G)*Oct_2023_AVG,3))
G_15thru21_SDev = round(G_15thru21_YEARLY_AVG['flow'].std(), 3)
print('std deviation =', G_15thru21_SDev)

#%%
## dropping the year 2005 because it is an outlier with a value of 155 cfs

F_15thru21_Yearly_Avg_Trimmed = F_15thru21_YEARLY_AVG.drop(F_15thru21_YEARLY_AVG[F_15thru21_YEARLY_AVG['year'] == 2005].index)
F_15thru12_trimmed_finalAVG = round(F_15thru21_Yearly_Avg_Trimmed['flow'].mean(),3)
print(F_15thru12_trimmed_finalAVG)

One_Week_out_prediction = F_15thru12_trimmed_finalAVG

#%%___________________________________________________________________________________________
## 2 WEEK OUT PREDICTIONS
F_flow_avg
years_of_int_F = F_flow_avg['year'].tolist()
F_22thru28_Flow_List = data[(data['month'] == 10) & 
                      (data['day'] >= 22) & 
                      (data['day'] <= 28) &
                      (data['year'].isin(years_of_int_F))] # historical avgs of Oct 22 - 28

F_22thru28_YEARLY_AVG = F_22thru28_Flow_List.groupby(['year'])[['flow']].mean().reset_index()


F_22thru28_AVG = round(F_22thru28_YEARLY_AVG['flow'].mean(),3)



print('this avg flow: October 22 - 28: prev 2 weeks w/in .35 of 2023 past 2 weeks average:')
print(F_22thru28_AVG)
print("this flow is between", round((1-Range_F)*Oct_2023_AVG,3) , "and", round((1+Range_F)*Oct_2023_AVG,3))
F_22thru28_SDev = round(F_22thru28_YEARLY_AVG['flow'].std(), 3)
print('std deviation =', F_22thru28_SDev)

#%%
F_22thru28_Yearly_Avg_Trimmed = F_22thru28_YEARLY_AVG.drop(F_22thru28_YEARLY_AVG[F_22thru28_YEARLY_AVG['flow'] > 170].index)
F_22thru28_trimmed_finalAVG = round(F_22thru28_Yearly_Avg_Trimmed['flow'].mean(),3)
print(F_22thru28_trimmed_finalAVG)


# %% GRAPH SECTION _________________________________________________________________________

# SCATTER PLOT -> Plotting Past 2 week historical data w/ October 15-21 flow average and 22-28 flow average


# %%

# %%

Oct_historic_AVG # average of flow in October 1 - 14
Oct_15thru21_2023_flow_AVG = (data[(data["month"] == 10) & 
                      (data['day'] >= 15) & 
                      (data['day'] <= 21)]).groupby(['year'])[['flow']].mean().reset_index()
Oct_22thru28_2023_flow_AVG = (data[(data["month"] == 10) & 
                      (data['day'] >= 22) & 
                      (data['day'] <= 28)]).groupby(['year'])[['flow']].mean().reset_index()

# %%
OneWk_Oct1_14_Comb = pd.DataFrame()

# Populate the new DataFrame with the 'year', 'Oct1thru14', and 'Oct14thru21' columns
OneWk_Oct1_14_Comb['year'] = Oct_historic_AVG['year']
OneWk_Oct1_14_Comb['Oct1thru14'] = Oct_historic_AVG['flow']
OneWk_Oct1_14_Comb['15thru21'] = Oct_15thru21_2023_flow_AVG['flow']

OneWk_Oct1_14_Comb
#%% 
TwoWk_Oct1_14_Comb = pd.DataFrame()

TwoWk_Oct1_14_Comb['year'] = Oct_historic_AVG['year']
TwoWk_Oct1_14_Comb['Oct1thru14'] = Oct_historic_AVG['flow']
TwoWk_Oct1_14_Comb['22thru28'] = Oct_22thru28_2023_flow_AVG['flow']

TwoWk_Oct1_14_Comb
# %%
x1 = OneWk_Oct1_14_Comb['Oct1thru14']
y1 = OneWk_Oct1_14_Comb['15thru21']
x2 = TwoWk_Oct1_14_Comb['Oct1thru14']
y2 = TwoWk_Oct1_14_Comb['22thru28']
fig, ax = plt.subplots()
ax.scatter(x1, y1, label='October 15th - 21st',color = 'yellow', marker='.')
ax.scatter(x2, y2, label='Octover 22nd - 28th', marker='.', color='r')
ax.legend()
ax.set_xlabel('Proceeding Weeks Flow Averages (CFS)')
ax.set_ylabel('October 1 - 14 Flow Averages (CFS)')
ax.set_title('Historical Averages of Oct 1 - 14 vs following two weeks')



z = np.polyfit(x1, y1, 1)
p = np.poly1d(z)
plt.plot(x1, p(x1), color="yellow", linewidth=.25, linestyle="--")

z = np.polyfit(x2, y2, 1)
p = np.poly1d(z)
plt.plot(x1, p(x1), color="red", linewidth=.25, linestyle="--")
plt.show()


# %%
Daily_Flow_Aug_to_Oct_2023 = data[(data["month"] >= 7) & (data["month"] <= 10) & (data["year"] == 2023)]
Daily_Flow_Aug_to_Oct_2023



Flow_Aug_Oct_2023_DF = pd.DataFrame({'flow': Daily_Flow_Aug_to_Oct_2023['flow']})

# Add a 'day' column with ascending numbers
Flow_Aug_Oct_2023_DF['day'] = range(1, len(Flow_Aug_Oct_2023_DF) + 1)

# Reset the index (if needed)
Flow_Aug_Oct_2023_DF.reset_index(drop=True, inplace=True)




#%%
x = Flow_Aug_Oct_2023_DF['day']
y = Flow_Aug_Oct_2023_DF['flow']
plt.style.use('dark_background')
ax = plt.axes()
plt.xlim(0,120)
ax.plot(x, y,)
ax.grid(linewidth=.25, which='both')
ax.plot(x[:31], y[:31], color='blue', label='July', linewidth = 1)
ax.plot(x[30:62], y[30:62], color='green', label='August',linewidth = 1)
ax.plot(x[61:93], y[61:93], color='yellow', label='September',linewidth = 1)
ax.plot(x[92:108], y[92:108], color='red', label='October',linewidth = 3)
ax.set_title('Daily Flow Averages: July - October 2023')
ax.set_xlabel('Days since July 1')
ax.set_ylabel('Daily Average Flow Rate (CFS)')


ax.legend(loc='upper right')
# %%
Flow_Aug_Oct_2023_DF.max()

#%%
# x = Daily_Flow_Aug_to_Oct_2023['datetime']
# y = Daily_Flow_Aug_to_Oct_2023['flow']
#plt.style.use('dark_background')
#x = plt.axes()
#ax.plot(x, y, label='-')

#ax.legend(loc='upper right')
# %% 4 Panel HISTOGRAM

## OCTOBER 15-22 Averages through years
# percentage range within the average of this years past Oct 1 - 14 

# 100%
Oct_historic_AVG

# 75%
Range_75 = .75
Rng75_flow_avg = Oct_historic_AVG[(Oct_historic_AVG['flow'] > ((1- Range_75)*Oct_2023_AVG)) & (Oct_historic_AVG['flow'] < ((1+Range_75)*Oct_2023_AVG))]
Rng75_flow_avg
# 40% (F -- used for flow prediction)
F_22thru28_YEARLY_AVG = F_22thru28_Flow_List.groupby(['year'])[['flow']].mean().reset_index()
F_22thru28_YEARLY_AVG
# 20%
C_flow_avg


#%%

fig, ((x1,x2),(x3, x4)) = plt.subplots(nrows = 2, ncols =2)


x1.hist(Oct_historic_AVG['year'], bins=len(Oct_historic_AVG['year']), weights=Oct_historic_AVG['flow'], color = 'red', edgecolor='yellow')
x2.hist(Rng75_flow_avg['year'], bins = len(Rng75_flow_avg['year']), weights=Rng75_flow_avg['flow'], color = 'green', edgecolor='yellow')
x3.hist(F_22thru28_YEARLY_AVG['year'], bins = len(F_22thru28_YEARLY_AVG['year']), weights=F_22thru28_YEARLY_AVG['flow'], color= 'pink', edgecolor='yellow')
x4.hist(C_flow_avg['year'], bins = len(F_22thru28_YEARLY_AVG['year']), weights=C_flow_avg['flow'], edgecolor='yellow')

x1.set_title("All Years October Averages",fontsize=6)
x2.set_title("Averages w/in 75%' of current October Average",fontsize=6)
x3.set_title("Averages w/in 40%' of current October Average",fontsize=6)
x4.set_title("Average w/in 20%' of current October Average",fontsize=6)

fig.supxlabel('Year', x=0.5, ha='center')
fig.supylabel('Flow (CFS)', y=0.5, ha='center')
fig.suptitle('Average October Flows w/in Varying Ranges of current 2023 October Flow')

plt.tight_layout()
plt.show()



# %%



# %%
Oct_daily_flow = data[(data["month"] == 10)].groupby(['day'])[['flow']].mean().reset_index()
# %%
plt.hist(Oct_daily_flow['day'], bins = 31, weights=Oct_daily_flow['flow'],edgecolor='red')

plt.xticks(range(1,32,3))
plt.ylim(100,200)
plt.title('Average Daily Flow in October: Data from 1989 - 2022')
plt.ylabel('Flow (CFS)')
plt.xlabel('Day')

plt.show()
# %%
Oct_daily_MAX = data[(data["month"] == 10)].groupby(['day'])[['flow']].max().reset_index()
Oct_daily_MIN = data[(data["month"] == 10)].groupby(['day'])[['flow']].min().reset_index()
Oct_daily_flow

xAv = Oct_daily_flow['day']
yAv = Oct_daily_flow['flow']
xMx = Oct_daily_MAX['day']
yMx = Oct_daily_MAX['flow']
xMn = Oct_daily_MIN['day']
yMn = Oct_daily_MIN['flow']
fig, ax = plt.subplots()
ax.scatter(xAv, yAv, label='Daily Avg Flow', marker='.',color = 'red',)
ax.scatter(xMx, yMx, label='Daily Max Flow', marker ='.', color='green')
ax.scatter(xMn, yMn, label='Daily Min Flow', marker ='.', color='yellow')

ax.plot(xAv, yAv, linestyle='-', color='red')
ax.plot(xMx, yMx, linestyle='-', color='green')
ax.plot(xMn, yMn, linestyle='-', color='yellow')


ax.legend()
ax.set_xlabel('Day in October')
ax.set_ylabel('Flow (CFS)')
ax.set_title('Average, Min, & Max Flow for days in October: data from 1989 - 2022')
# %%
