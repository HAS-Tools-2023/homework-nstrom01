
#%%

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



data = pd.read_table('Verde_flow_wk8.txt', sep='\t', skiprows=30,
                      names =['agency_cd', 'site_no',
                              'datetime', 'flow', 'code'],index_col=['datetime'],
                              parse_dates =['datetime'])


#%%
OctNov_2023_flow = data.loc['2023'].loc['2023-10-01':'2023-11-10']['flow']
OctNov_2022_flow = data.loc['2022'].loc['2022-10-01':'2022-11-10']['flow']
OctNov_2021_flow = data.loc['2021'].loc['2021-10-01':'2021-11-10']['flow']
OctNov_2020_flow = data.loc['2020'].loc['2020-10-01':'2020-11-10']['flow']
# %%

fig, ax = plt.subplots(2,2, sharey='all')
fig.supylabel('Daily Avg Flow (CFS)')
fig.supxlabel('Day (Oct 01 - Nov 10)')
fig.suptitle('Daily Flow Trends in October 01 - Novemeber 10') 

ax[0,0].plot(OctNov_2023_flow, 'r')
ax[0,1].plot(OctNov_2022_flow, 'y')
ax[1,0].plot(OctNov_2021_flow, 'g')
ax[1,1].plot(OctNov_2020_flow, 'b')

ax[0,0].title.set_text('2023')
ax[0,1].title.set_text('2022')
ax[1,0].title.set_text('2021')
ax[1,1].title.set_text('2020')

for row in ax:
    for subplot in row:
        subplot.set_xticklabels([]) # removing the day labels b/c they are too cramped

plt.tight_layout()

#%%

#%%
# %% Making the Correction factors from the error of previous predictions

wk_5_act = 67.3
wk_6_act = 66.571
wk_7_act = 77.457

wk_5_prdct = 105
wk_6_prdct = 99
wk_7_prdct = 105

correction_factor = (((wk_7_act/data.loc['2023-10-20']['flow']))) # + 0.25*(wk_7_act/wk_7_prdct))+(0.15*(wk_6_act/wk_6_prdct))+(0.10*(wk_5_act/wk_5_prdct))
# %%
Oct2023_8th21 = data.loc['2023-10-08':'2023-10-21']
Avg_2023_O8th21 = Oct2023_8th21['flow'].mean()


# %%
Oct8t21_all = data[(data.index.month == 10) & (data.index.day >= 8) & (data.index.day <= 21)]

Oct8_21_AVG_all_flow = Oct8t21_all.groupby(Oct8t21_all.index.year)[['flow']].mean()

# %%
Range_F = .40
Oct_match_years = Oct8_21_AVG_all_flow[(Oct8_21_AVG_all_flow['flow'] > ((1- Range_F)*Avg_2023_O8th21)) & ((Oct8_21_AVG_all_flow['flow'] < ((1+Range_F)*Avg_2023_O8th21)))]

# %%
Year_range = Oct_match_years.index.tolist()
O22t28_years = data[(data.index.month == 10)
                     & (data.index.day >= 22)
                       & (data.index.day <= 28) & 
                       (data.index.year.isin(Year_range))]
# %%

# %%
weekly = data['flow'].resample('W').sum()
weekly.plot()

#%%
O22t28_year_flow = O22t28_years.groupby(O22t28_years.index.year)[['flow']].mean()
# %%
#Oct29thNov04_historical = data.loc['1989-10-29':'2023-11-04']
Oct_22th28_historical = data[(data.index.month == 10)
                     & (data.index.day >= 22)
                       & (data.index.day <= 28)]


#%%
Year_range 
Oct28_Nov04_Historical_ALL = data[((data.index.month == 10) & (data.index.day >= 29) |
                   (data.index.month == 11) & (data.index.day <= 4))]

Oct28_Nov04_inRange = data[((data.index.month == 10) & (data.index.day >= 29) |
                   (data.index.month == 11) & (data.index.day <= 4)) & 
                   data.index.year.isin(Year_range)]

Oct28_Nov04_avg_flow = Oct28_Nov04_inRange.groupby(Oct28_Nov04_inRange.index.year)[["flow"]].mean()



wk2_flow_mean = Oct28_Nov04_avg_flow['flow'].mean()
x = Oct28_Nov04_avg_flow[Oct28_Nov04_avg_flow['flow'] < 120]

wk2_flow_mean_trimmed = x['flow'].mean()



#Oct_Nov_flow = O22t28_years.groupby(O22t28_years.index.year)[['flow']].mean()
# %%
#Oct29thNov04_historical = data.loc['1989-10-29':'2023-11-04']
Oct_22th28_historical = data[(data.index.month == 10)
                     & (data.index.day >= 22)
                       & (data.index.day <= 28)]
# %%
plt.style.use('seaborn-v0_8-darkgrid')
Oct_22th28_historical['flow'].plot(color = 'red',label = 'all years included')
O22t28_years['flow'].plot(color = 'blue', style ='.',label = 'years w/ in 2023 calculated range')
plt.xlabel('Year')
plt.ylabel('Average Daily Flow')
plt.title('Historical Flow: Oct 22 - 28')
plt.legend()
#%%
plt.style.use('seaborn-v0_8-darkgrid')
Oct28_Nov04_Historical_ALL['flow'].plot(label = 'all years included',color = 'red')
Oct28_Nov04_inRange['flow'].plot(color = 'blue', style ='.', label = 'years w/ in 2023 calculated range')
plt.xlabel('Year')
plt.ylabel('Average Daily Flow')
plt.title('Historical Flow: Oct 29 - November 04')
plt.legend()
# %%
Trimmed_wk1_prdct_list = O22t28_year_flow[(O22t28_year_flow["flow"] < 200)]
wk1_flow_mean = Trimmed_wk1_prdct_list["flow"].mean()


# %%
wk_1_prediction = round((wk1_flow_mean*correction_factor),1)
# %%
# Graph shows historical trends of higher flow november


wk_2_prediction = round((wk2_flow_mean_trimmed*(correction_factor+.1)),1)
# %%

print('THE PREDICTED AVG FLOW FOR 1 WEEK OUT (dates 10/22-28) IS...',wk_1_prediction, 'cfs')




print('THE PREDICTED AVG FLOW FOR 2 WEEKS OUT (dates 10/29-11/04) IS...',wk_2_prediction, 'cfs')
# %%
