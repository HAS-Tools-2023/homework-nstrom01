#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
x1 = [1, 2, 3, 4, 5]
y1 = [2,5,8,11,10]
x2 = [1, 2, 3, 4, 5]
y2 = [18,12,3,5,10]
fig, ax = plt.subplots()
ax.scatter(x1, y1, label='Dataset 1')
ax.scatter(x2, y2, label='Dataset 2', marker='x', color='r')
ax.legend()
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Multiple Datasets Scatter Plot')
plt.show()

#%%
## Import the flow data to use
data = pd.read_table("./streamflow_demo.txt",  sep='\t', skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'])
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

## Plot 1: Simple line plot
x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
y1=np.sin(x)
y2=np.cos(x)
plt.style.use('classic')
ax = plt.axes()
ax.plot(x, y1, linestyle='dashed', label='sinx')
ax.plot(x, y2, label='cosx')
ax.legend(loc='upper right')


## Plot 2: Scatter Plot
plt.style.use('default')
ax=data.plot.scatter(x='month', y='flow',
                     c='year', colormap='viridis', marker='x')
ax.set_title("Monthly stream Flow")

#%%

## Plot 3: Histogram 
mybins = np.linspace(0, np.log10(np.max(data["flow"])), num=15)
plt.hist(np.log10(data["flow"]), bins=mybins)
plt.title('Streamflow')
plt.ylabel('Count')
#%%

## Plot 4: Filled plot
monthly_max = data.groupby(data.month).max()
monthly_min = data.groupby(data.month).min()
monthly_mean = data.groupby(data.month)["flow"].mean()

ax = plt.axes()
ax.plot(monthly_mean)
ax.fill_between(monthly_min.flow.index,
                monthly_min.flow.values, monthly_max.flow.values, alpha=0.2)
ax.set_yscale("log")
ax.set_xlabel("month")
plt.axvline(3, color='black', linestyle='--')
# %%




#%% 


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')


#%%

## Import the flow data to use
data = pd.read_table("Wk8_Verde_Data.txt",  sep='\t', skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'])
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)



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
ax.scatter(x2, y2, label='Octover 22nd - 28th', marker='x', color='r')
ax.legend()
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Historical Averages of Oct 1 - 14 vs following two weeks')



z = np.polyfit(x1, y1, 1)
p = np.poly1d(z)
plt.plot(x1, p(x1), color="yellow", linewidth=.5, linestyle="-")

z = np.polyfit(x2, y2, 1)
p = np.poly1d(z)
plt.plot(x1, p(x1), color="red", linewidth=.5, linestyle="--")
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
ax.plot(x, y,)
ax.plot(x[:31], y[:31], color='blue', label='July')
ax.plot(x[30:62], y[30:62], color='yellow', label='August')
ax.plot(x[62:93], y[62:93], color='red', label='September')
ax.plot(x[93:108], y[93:108], color='green', label='July')


ax.legend(loc='upper right')
# %%
Flow_Aug_Oct_2023_DF.max()

# %%
#%%
x = Daily_Flow_Aug_to_Oct_2023['datetime']
y = Daily_Flow_Aug_to_Oct_2023['flow']
plt.style.use('dark_background')
ax = plt.axes()
ax.plot(x, y, label='-')

ax.legend(loc='upper right')
# %%
## Histogram of Entire Historical Data

