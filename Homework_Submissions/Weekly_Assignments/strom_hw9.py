# %% 
# PASTED FROM HW #8 as of 10/28 has not been changed
# LC p you don't need this comment. 
import pandas as pd
import matplotlib.pyplot as plt

# %% 
# Importing and reading flow data. Setting data up as a datetime compatible dataframe

# LC the ____ ad the end of your comment line were too long and made it hard to read I would get rid of these. 
# Also I would put the # %% break on its own line


data = pd.read_table('Verde_flow_wk9.txt', sep='\t', skiprows=30,
                      names =['agency_cd', 'site_no',
                              'datetime', 'flow', 'code'],index_col=['datetime'],
                              parse_dates =['datetime'])
#%% 
# WRITTING FUNCTIONS TO USE THROUGHOUT CODE
#LC I put all of your functions into one cell 

#LC excellent doc strings!
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
    function_data = DATA[(DATA.index.year == YEAR) & ((DATA.index.month == 10) | (DATA.index.month == 11))]['flow']

    return function_data

#LC -- note that I moved your doc strings up to the top of the function where they must be. 
# also note i added white spaces between your lines to make them easier to folow


#LC This function is good but you can do this much more simply just using the dates in their entirety like this: 
flow_2023 = df[(df.index >='2023-08-28') & (df.index <='2023-10-28')]

def get_flow_total_flow_from_daterange(DATA, year_start, month_start, day_start, year_end, month_end, day_end):
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
  df_year = DATA[(DATA.index.year >= year_start) & (DATA.index.month <= year_end)]

  df_month = df_year[((df_year.index.month >= month_start) & (df_year.index.month <= month_end))]

  df_output = df_month.drop(df_month.index[(df_month.index.month == month_start) & (df_month.index.day < day_start)])

  df_output = df_output.drop(df_output.index[(df_output.index.month == month_end) & (df_output.index.day > day_end)])

  return df_output


#LC - note that you should use tabs not spaces for indenting things in python 

#LC - see comment above for how you can simlify your function. YOu could also use the outputs of the function above as inputs to this so you don't need to do the date range filtering more than once. 
def flow_mean_by_daterange(data_frame, year_start, month_start, day_start, year_end, month_end, day_end):
  """ Creates a dataframe of flow mean grouped by year  for the specified date range input. 
    Returns
    _____________________
    output: Pandas dataframe     
  """
  df_year = data_frame[(data_frame.index.year >= year_start) & (data_frame.index.month <= year_end)]

  df_month = df_year[((df_year.index.month >= month_start) & (df_year.index.month <= month_end))]

  df_output = df_month.drop(df_month.index[(df_month.index.month == month_start) & (df_month.index.day < day_start)])

  df_output = df_output.drop(df_output.index[(df_output.index.month == month_end) & (df_output.index.day > day_end)])

  df_output = df_output.groupby(df_output.index.year)[['flow']].mean()
  
  return df_output

def get_total_mean_from_df(df):
  """ Use a variable that contains a defined dataframe that is in datetime, and has a year column that corresponds with a flow column
        Function will take the dataframe variable input, and find the sum of all flow across all rows
  
    Returns
    _____________________
    output: float -- total mean of all flow
  """
  df_output = df.groupby(df.index.year)[['flow']].mean()['flow'].mean()

  return df_output

# %% 
# FORECAST PREDICTION CALCULATIONS_
# LC- your note is good but you need a bigger picture comment explaining what is happening in this cell 

# This correction factor paired with this method worked well for last weeks prediction -- will use the same correction factor
  # As this years Fall flow is exceptionally low, this correction factor attempts to correct for this methods tendency to over predict the flow value 
WK_7_ACTUAL_FLOW = 77.46
Oct_20_2023_flow = get_flow_total_flow_from_daterange(data, 2023, 10, 20, 2023, 10, 20)['flow'].mean()
correction_factor = (WK_7_ACTUAL_FLOW/Oct_20_2023_flow)

#%% 
# Finding the historical flow means of the 1 week out and 2 week prediction date ranges

#your variable names are clear by very long. Consider how you can shorten them
Oct29thruNov04_mean_flow_byYr = flow_mean_by_daterange(data, 1989, 10, 29, 2023, 11, 4)
Oct29thruNov04_historical_totalMean = Oct29thruNov04_mean_flow_byYr['flow'].mean()

Nov05thru11_mean_flow_byYr = flow_mean_by_daterange(data, 1989, 11, 5, 2023, 11, 11)
Nov05thru11_historical_totalMean = Nov05thru11_mean_flow_byYr['flow'].mean()

# %% 
# Finding the past current 10 days flow of this year (October 20-28, 2023)
Avg2023_Oct20thru28_flow = get_flow_total_flow_from_daterange(data, 2023, 10, 20, 2023, 10, 28)
Oct20thru28_2023_mean = Avg2023_Oct20thru28_flow['flow'].mean()

all_flow_avg_Oct29thruNov04 = get_flow_total_flow_from_daterange(data, 1989, 10, 28, 2023, 11, 4)
all_flow_avg_Oct20thru28 = get_flow_total_flow_from_daterange(data, 1989, 10, 20, 2023, 10, 28)

#%%
# LC - Need a comment here explaining the purpose of this cell 

AVG_RANGE_FOURTY_PERCENT = .40 # this is the range (+/- 40%) which the flow averages are matched to select for and create the prediction flow value for this week and 2 weeks out

#LC if you have calls going onto multiple lines you should have white space between them so it can be broken up a bit. 
Match_years = all_flow_avg_Oct20thru28[(all_flow_avg_Oct20thru28  ['flow'] > ((1- AVG_RANGE_FOURTY_PERCENT)*Oct20thru28_2023_mean)) & ((all_flow_avg_Oct20thru28['flow'] < ((1+AVG_RANGE_FOURTY_PERCENT)*Oct20thru28_2023_mean)))]

Years = Match_years.groupby(Match_years.index.year)[['flow']].mean()
Year_range = Years.index.tolist() # years are added to a list so they do not have to be repeated when the following conditional variables are defined

#LC need to have white space at the end of your code blocks so you can see the breaks

# %% Finding the 1 week out prediction before correction
Oct29toNov04_inRange_DF = data[(((data.index.month == 10) & (data.index.day >= 29) & (data.index.day <= 31)) |((data.index.month == 11) & (data.index.day <= 4))) & (data.index.year.isin(Year_range))]

wk_1_prediction_b4_correction = get_total_mean_from_df(Oct29toNov04_inRange_DF)

#%% Finding the 2 week out prediction before correction 
Nov_5thru11_inRange_DF = data[(((data.index.month == 11) & (data.index.day >= 5) & (data.index.day <= 11))) & data.index.year.isin(Year_range)]

wk_2_prediction_b4_correction = get_total_mean_from_df(Nov_5thru11_inRange_DF)
# %%

#LC looks like you have a blank cell here



#%% 
# Correction factors were further adjusted for each speccific data point based upon intuition
wk_1_prediction = round(wk_1_prediction_b4_correction*(correction_factor-.15),1)
wk_2_prediction = round(wk_2_prediction_b4_correction*(correction_factor-.05),1)

print('THE PREDICTED AVG FLOW FOR 1 WEEK OUT (dates 10/29-11/04) IS...',wk_1_prediction, 'cfs')
print('THE PREDICTED AVG FLOW FOR 2 WEEKS OUT (dates 11/05-11/11) IS...',wk_2_prediction, 'cfs')


#%% 
# PLOTTING DATA

# Defining dataframes to plot for visualizing trends in the past 4 years of October and November
Oct_Nov_2023_flow = get_Oct_Nov_DailyFlow_by_Year(2023,data)
Oct_Nov_2022_flow = get_Oct_Nov_DailyFlow_by_Year(2022,data)
Oct_Nov_2021_flow = get_Oct_Nov_DailyFlow_by_Year(2021,data)
Oct_Nov_2020_flow = get_Oct_Nov_DailyFlow_by_Year(2020,data)


#%% Subplot of October and November flows
fig, ax = plt.subplots(2,2, sharey='all') 
fig.supylabel('Daily Avg Flow (CFS)')
fig.supxlabel('Day (Oct 01 - Nov 10)')
fig.suptitle('Daily Flow Trends in October 01 - Novemeber 10') 
   
ax[0,0].plot(Oct_Nov_2023_flow, 'r')
ax[0,1].plot(Oct_Nov_2022_flow, 'y')
ax[1,0].plot(Oct_Nov_2021_flow, 'g')
ax[1,1].plot(Oct_Nov_2020_flow, 'b')

ax[0,0].title.set_text('2023')
ax[0,1].title.set_text('2022')
ax[1,0].title.set_text('2021')
ax[1,1].title.set_text('2020')
plt.tight_layout()

# %%
#LC - needs a comment
Oct29thruNov04_mean_flow_byYr = flow_mean_by_daterange(data, 1989, 10, 28, 2023, 11, 4)

plt.style.use('seaborn-v0_8-darkgrid')

Oct29thruNov04_mean_flow_byYr['flow'].plot(color = 'red',label = 'all years included')

Years['flow'].plot(color = 'blue', style ='.',label = 'years w/ in 2023 calculated range')

plt.xlabel('Year')
plt.ylabel('Average Daily Flow')
plt.title('Historical Flow: Oct 22 - 28')
plt.legend()
#%%
# LC Needs a comment
Nov05thru11_mean_flow_byYr = flow_mean_by_daterange(data, 1989, 11, 5, 2023, 11, 11)

plt.style.use('seaborn-v0_8-darkgrid')
Nov05thru11_mean_flow_byYr['flow'].plot(label = 'all years included',color = 'red')
Years['flow'].plot(color = 'blue', style ='.', label = 'years w/ in 2023 calculated range')
plt.xlabel('Year')
plt.ylabel('Average Daily Flow')
plt.title('Historical Flow: Oct 29 - November 04')
plt.legend()
# %%
# Graph shows historical trends of higher flow november
weekly = data['flow'].resample('W').sum()
weekly.plot()

