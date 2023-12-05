
#%%
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


#%%


"""
Enter the Monday date of the forecast week of interest.
A prediction of the average flow for the entered week and the following week will print.
"""
forecast_date_week1 = '2023-11-27'

#LC reflecting on your comments. In my opinion your code would be easier to read without this outer function. Instead I would just definite the inner functions up top and then do the actions of this outer function (ie. find_streamflow_prediction_from_usgs_stream) within the main script.  

# This is not to say that functions calling functions is a no-go in general (and if this class went for another semester we would start talking about building classes) but in this case because everything just ended up being one big function it made it a bit more confusing in my opinion. 

def find_streamflow_prediction_from_usgs_stream(site_number='09506000',
                                                data_start_date='1989-01-01',
                                                data_end_date='2023-11-25',
                                                wk1_predict_date='2023-11-27',
                                                trim_range=.5, std_size=1):
    """
    Predicts streamflow based on historical data.

    Inputs:
    - site_number (str): USGS site number.
    - data_start_date (str): Start date for historical data.
    - data_end_date (str): End date for historical data.
    - wk1_predict_date (str): Date for the one-week prediction.
    - trim_range (float): Range for trimming similar flow years.
    - std_size (int): Multiplier for standard deviation.

    Outputs: tuple: A tuple containing two elements:
    - float: One week out flow prediction.
    - float: Two week out flow prediction.
    - plot: Historical flow averages w/ forecast averages


    Inner Functions:
    - 'find_yearly_flow_mean': Finds the yearly mean flow for a given date range.
    - 'find_flow_forecast_by_week': Finds the flow forecast for a given week.
    - 'plot_week_flow_avg_by_year': Plots weekly avgs and forecast avgs

    Description:
        Predicts streamflow based on historical data for a specified site and date range. 
        Calcs dates, computes datasets, finds similar flow years, 
        and predicts flow for 1 and 2 wks out.


    Note: All inner functions are used to support the main prediction functionality.
        A smaller 'trim_range' & 'std_size' does not always yield a smaller forecast. 
    """

    # Reading in file from URL and setting data
    url = (
        "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" 
        + site_number
        + "&referred_module=sw&period=&begin_date=" 
        + data_start_date + "&end_date=" 
        + data_end_date)
    data = pd.read_table(
        url, skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime'],
        index_col=['datetime'])

    # Setting the dates needed for dataframes from the input wk1 date
    # LC - Nice job useing the pd.DateOffset function here this is a very clean way to do this!
    wk1_predict_date = pd.to_datetime(wk1_predict_date)
    pst_2wk_strt_d8 = wk1_predict_date - pd.DateOffset(days=15)
    last_day_d8 = wk1_predict_date - pd.DateOffset(days=1)
    wk2_predict_d8 = wk1_predict_date + pd.DateOffset(days=7)
    crnt_yr = last_day_d8.year
    wk1_predict_yr = wk1_predict_date.year
    wk2_predict_yr = wk2_predict_d8.year

    # Making datasets that will be used for calc later in code
    # LC its usually best practice to put all of your functions at the top of a script rather than having them be distributed throughout. In this case you could put them all at the top of this outer function. 
    def find_yearly_flow_mean(df=data, start_date=pst_2wk_strt_d8,
                              end_date=last_day_d8):
        """
        Finds the yearly mean flow for a given date range.

        Inputs:
        - df (pd.DataFrame): Input DataFrame.
        - start_date (pd.Timestamp): Start date.
        - end_date (pd.Timestamp): End date.

        Output:
        pd.DataFrame: DataFrame with yearly mean flow for defined dates.

        Description: Calculates the yearly mean flow for a given date range from a DataFrame. 
        Groups by year, computes mean flow, and returns a DataFrame.
        """
        # LC Tese next few lines could probably be variables you skip defining since they are only used at most twice and because `start_date.month` is actually more interpretable than `strt_mnth`
        strt_mnth = start_date.month,
        end_mnth = end_date.month
        strt_day = start_date.day
        end_day = end_date.day

        # Creating dataframe from input dates
        if strt_mnth == end_mnth:
            select_df = df[(df.index.month == strt_mnth) &
                           (df.index.day >= strt_day) & 
                           (df.index.day <= end_day)] 
        else:
            select_df = df[((df.index.month == strt_mnth) &
                            (df.index.day >= strt_day)) |
                           ((df.index.month == end_mnth) &
                            (df.index.day <= end_day))]
        df_mean_by_year = (
            select_df.groupby(select_df.index.year)[['flow']].mean())
        df_mean_by_year.index = (
            pd.to_datetime(df_mean_by_year.index, format='%Y'))
        df_mean_by_year.index.name = 'year'
        return (df_mean_by_year)

    # Using function to create dataframes that will be used for forecasts
    pst2wk_mean_df = find_yearly_flow_mean(
        start_date=pst_2wk_strt_d8, end_date=last_day_d8)
    wk1_hist_mean_df = find_yearly_flow_mean(
        start_date=wk1_predict_date,
        end_date=(wk2_predict_d8 - pd.DateOffset(days=1)))
    wk2_hist_mean_df = find_yearly_flow_mean(
        start_date=wk2_predict_d8, 
        end_date=(wk2_predict_d8 + pd.DateOffset(days=6)))

    # Finding similar flow yrs from historical past 2 wks & trim_range input
    crnt_yr_pst2wk_mean = pst2wk_mean_df[
        (pst2wk_mean_df.index.year == crnt_yr)].iloc[0, 0]
    up_bound = crnt_yr_pst2wk_mean*(1+trim_range)
    low_bound = crnt_yr_pst2wk_mean*(1-trim_range)
    year_list = (pst2wk_mean_df[(pst2wk_mean_df['flow'] <= up_bound) &
                                (pst2wk_mean_df['flow'] >=
                                 low_bound)]).index.tolist()

    # Taking DFs from above function and finding a forecast w/in input StdDev
    # LC Its not a good idea when you setup your function to have default values that are equal to some variable inside your script (e.g. week_df = wk1_hist_mean_df) this will break if you try to run it in another setting). 
    # You have two options to avoid this. 
    # 1. You can either not define default values when you setup your function in which case your function definition would look like this: def find_flow_forecast_by_week(week_df, year_list). If you do it this way the user has to put in values for those funciton arguments when they call the function. This is a totally fine expectation. 
    # 2. you can define default options but then they should be actual values not variables. You did this in your first fuction when you said site_number='09506000'
    def find_flow_forecast_by_week(
            week_df=wk1_hist_mean_df, year_list=year_list):
        """
        Finds the flow forecast for a given week.

        Inputs:
         - week_df (pd.DataFrame): DataFrame for the week.
         - year_list (list): List of years to consider.

        Output:
            float: Flow forecast for the week.

        Description:
            Forecasts flow for a specific week based on historical data. 
            Filters relevant years, determines a flow range, 
                and predicts the mean flow for the week.
         """
        in_years_df = week_df[(week_df.index.isin(year_list))]
        range = ((in_years_df['flow'].std())*(std_size))/2
        upr_bnd = (in_years_df['flow'].mean()) + range
        flow_predict = round(in_years_df[(in_years_df['flow'] <= upr_bnd)]
                             ['flow'].mean(), 1)
        return flow_predict

    forecast_1wk = find_flow_forecast_by_week()
    forecast_2wk = find_flow_forecast_by_week(week_df=wk2_hist_mean_df)

    # Creating plots of historical & forecast for visual reference 
    def plot_week_flow_avg_by_year():
        """Plots Historical and forecasted weekly avg flow within the 1 week & 2 week out dates

        Inputs (all automatically input from above functions):
            - forecast_1wk
            - wk1_predict_yr
            - forecast_2wk
            - wk2_predict_yr
            - wk1_hist_mean_df
            - wk2_hist_mean_df

        Output:
            - Plot of weekly historical avgs and forecasts, years used for forecast calcs

        """
        wk1_predict_df = pd.DataFrame({'flow': [forecast_1wk]}, 
                                      index=[datetime(wk1_predict_yr, 1, 1)])
        wk1_predict_df.index.name = 'year'
        wk2_predict_df = pd.DataFrame({'flow': [forecast_2wk]}, 
                                      index=[datetime(wk2_predict_yr, 1, 1)])
        wk2_predict_df.index.name = 'year'

        #plt.style.use('seaborn-v0_8-darkgrid')
        wk1_hist_mean_df['flow'].plot(label='Historical week of ' +
                                      (wk1_predict_date.strftime('%m-%d')),
                                      color='red')
        wk1_predict_df['flow'].plot(
            label=wk1_predict_date.strftime('%m-%d-%y'),
            color='red', marker='o', markersize=3)
        wk2_hist_mean_df['flow'].plot(label='Historical week of ' +
                                      (wk2_predict_d8.strftime('%m-%d')),
                                      color='blue')
        wk2_predict_df['flow'].plot(label=wk2_predict_d8.strftime('%m-%d-%y'),
                                    color='blue', marker='o', markersize=3)

        # Plotting years that were used for forecast calc
        for year in year_list:
            plt.scatter(year, 0, color='black', marker="|", s=5)  
        plt.xlim(datetime(1989, 1, 1), datetime(2025, 1, 1))
        plt.legend()        
        plt.xlabel('Year')
        plt.ylabel('Avg Weekly Flow (CFS)')
        plt.title('Weekly Average and Forecast Flows for the weeks of ' +
                  (wk1_predict_date.strftime('%m-%d')) +
                  ' & ' + (wk2_predict_d8.strftime('%m-%d')))
    plot_week_flow_avg_by_year()

    print("Forecast for week of", wk1_predict_date.date(), "(wk1):",
          forecast_1wk, "cfs")
    print("Forecast for week of", wk2_predict_d8.date(), "(wk2):",
          forecast_2wk, "cfs")


find_streamflow_prediction_from_usgs_stream(
    wk1_predict_date=forecast_date_week1)


# %%
