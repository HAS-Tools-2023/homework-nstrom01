#%% PASTED FROM HW #8 as of 10/28 has not been changed
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%% Importing and reading flow data. Setting data up as a datetime compatible dataframe_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
data = pd.read_table('verde_flow_wk11.txt', sep='\t', skiprows=30,
                      names =['agency_cd', 'site_no',
                              'datetime', 'flow', 'code'],index_col=['datetime'],
                              parse_dates =['datetime'])
#%% WRITTING FUNCTIONS TO USE THROUGHOUT CODE_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def get_Oct_Nov_DailyFlow_by_Year(YEAR, DATA):
    """ Finds dataframe of the October and November flow of a given year that is input
    Data frame used must be in datetime, must have a column called 'flow' wiht corresponding months and years
    
    Parameters
    _____________________
    input: int
          Year that is associated with flow in selected dataframe
    
    Returns
    _____________________
    output: Pandas dataframe of 1D -- "Pandas Series" 
          
    """
    function_data = DATA[(DATA.index.year == YEAR) & ((DATA.index.month == 11))]['flow']
    return function_data
#%%
def get_flow_total_flow_from_daterange(DATA, year_start, month_start, day_start, year_end, month_end, day_end):
  df_year = DATA[(DATA.index.year >= year_start) & (DATA.index.month <= year_end)]
  df_month = df_year[((df_year.index.month >= month_start) & (df_year.index.month <= month_end))]
  df_output = df_month.drop(df_month.index[(df_month.index.month == month_start) & (df_month.index.day < day_start)])
  df_output = df_output.drop(df_output.index[(df_output.index.month == month_end) & (df_output.index.day > day_end)])
  return df_output
  """ Finds data frame defined by the inputs of the start year, month and day, and the data frame ends at the input end dates
      *** DOES NOT WORK FOR A MONTH RANGE THAT USES A month_start INTEGER THAT IS > month_start (ex: month_start: 11, month_end: 2)
    Data frame used must be in datetime, must have a column called 'flow' wiht corresponding months and years
    
    Parameters
    _____________________
    input: int
          Year that is associated with flow in selected dataframe
    
    Returns
    _____________________
    output: Pandas dataframe
          
    """
# Sample scripts to use for testing code
  # get_flow_total_flow_from_daterange(data, 2000, 9, 1, 2005, 10, 5).iloc[40:80,:]
  # get_flow_total_flow_from_daterange(data, 1998, 11, 30, 2005, 1, 4).iloc[100:160,:] -- code is broken for resetting months (IE December going to January 12 to 1, only use this function for consecutive months)
#%%
def flow_mean_by_daterange(data_frame, year_start, month_start, day_start, year_end, month_end, day_end):
  df_year = data_frame[(data_frame.index.year >= year_start) & (data_frame.index.month <= year_end)]
  df_month = df_year[((df_year.index.month >= month_start) & (df_year.index.month <= month_end))]
  df_output = df_month.drop(df_month.index[(df_month.index.month == month_start) & (df_month.index.day < day_start)])
  df_output = df_output.drop(df_output.index[(df_output.index.month == month_end) & (df_output.index.day > day_end)])
  df_output = df_output.groupby(df_output.index.year)[['flow']].mean()
  return df_output
""" Creates a dataframe of flow mean grouped by year for the specified date range input. 
  
    Returns
    _____________________
    output: Pandas dataframe
          
"""
#%%
def get_total_mean_from_df(df):
   df_output = df.groupby(df.index.year)[['flow']].mean()['flow'].mean()
   return df_output
   """ Use a variable that contains a defined dataframe that is in datetime, and has a year column that corresponds with a flow column
        Function will take the dataframe variable input, and find the sum of all flow across all rows
  
    Returns
    _____________________
    output: float -- total mean of all flow
          
"""

#%% FORECAST PREDICTION CALCULATIONS_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# This correction factor paired with this method worked well for last weeks prediction -- will use the same correction factor
  # As this years Fall flow is exceptionally low, this correction factor attempts to correct for this methods tendency to over predict the flow value 
WK_7_ACTUAL_FLOW = 77.46
Oct_20_2023_flow = get_flow_total_flow_from_daterange(data, 2023, 10, 20, 2023, 10, 20)['flow'].mean()
correction_factor = (WK_7_ACTUAL_FLOW/Oct_20_2023_flow)
#%% Finding the historical flow means of the 1 week out and 2 week prediction date ranges
Oct29thruNov04_mean_flow_byYr = flow_mean_by_daterange(data, 1989, 11, 12, 2023, 11, 18)
Oct29thruNov04_historical_totalMean = Oct29thruNov04_mean_flow_byYr['flow'].mean()

Nov05thru11_mean_flow_byYr = flow_mean_by_daterange(data, 1989, 11, 19, 2023, 11, 25)
Nov05thru11_historical_totalMean = Nov05thru11_mean_flow_byYr['flow'].mean()

# %% Finding the past current 10 days flow of this year (October 20-28, 2023)
Avg2023_Oct20thru28_flow = get_flow_total_flow_from_daterange(data, 2023, 11, 1, 2023, 11, 12)
Oct20thru28_2023_mean = Avg2023_Oct20thru28_flow['flow'].mean()

all_flow_avg_Oct29thruNov04 = get_flow_total_flow_from_daterange(data, 1989, 11, 12, 2023, 11, 18)
all_flow_avg_Oct20thru28 = get_flow_total_flow_from_daterange(data, 1989, 11, 19, 2023, 11, 25)

#%%
AVG_RANGE_FOURTY_PERCENT = .40 # this is the range (+/- 40%) which the flow averages are matched to select for and create the prediction flow value for this week and 2 weeks out
Match_years = all_flow_avg_Oct20thru28[(all_flow_avg_Oct20thru28['flow'] > ((1- AVG_RANGE_FOURTY_PERCENT)*Oct20thru28_2023_mean)) & ((all_flow_avg_Oct20thru28['flow'] < ((1+AVG_RANGE_FOURTY_PERCENT)*Oct20thru28_2023_mean)))]
Years = Match_years.groupby(Match_years.index.year)[['flow']].mean()
Year_range = Years.index.tolist() # years are added to a list so they do not have to be repeated when the following conditional variables are defined
# %% Finding the 1 week out prediction before correction
Oct29toNov04_inRange_DF = data[(((data.index.month == 11) & (data.index.day >= 12) & (data.index.day <= 18))) & (data.index.year.isin(Year_range))]
wk_1_prediction_b4_correction = get_total_mean_from_df(Oct29toNov04_inRange_DF)

#%% Finding the 2 week out prediction before correction 
Nov_5thru11_inRange_DF = data[(((data.index.month == 11) & (data.index.day >= 19) & (data.index.day <= 25))) & data.index.year.isin(Year_range)]
wk_2_prediction_b4_correction = get_total_mean_from_df(Nov_5thru11_inRange_DF)
# %%





#%% Correction factors were further adjusted for each speccific data point based upon intuition
wk_1_prediction = round(wk_1_prediction_b4_correction*(correction_factor+.1),1)
wk_2_prediction = round(wk_2_prediction_b4_correction*(correction_factor-.12),1)

print('THE PREDICTED AVG FLOW FOR 1 WEEK OUT IS...',wk_1_prediction, 'cfs')
print('THE PREDICTED AVG FLOW FOR 2 WEEKS OUT IS...',wk_2_prediction, 'cfs')

# %%
