
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json 
#%%

#%%
def find_streamflow_prediction_fromUSGS_stream(site_number = '09506000', data_start_date = '1989-01-01', data_end_date ='2023-11-18',
                                               start_date_week1_prediction = '2023-11-19', start_date_week2_prediction = '2023-11-26',
                                               trim_range = .7, std_dev_size = 2, last_day = 18):
        # reading in file from URL
        url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site_number + \
      "&referred_module=sw&period=&begin_date=" + data_start_date + "&end_date=" + data_end_date 
        DATA = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no', 
                                                    'datetime', 'flow', 'code'],parse_dates=['datetime'], 
                                                    index_col=['datetime'])
        
        # finding average flow of the past two weeks
        strt_d8_wk1_prediction = pd.to_datetime(start_date_week1_prediction)
        strt_d8_2wk_b4 = strt_d8_wk1_prediction - pd.DateOffset(days=14)
        strt_d8_1day_b4 = strt_d8_wk1_prediction - pd.DateOffset(days=1)
        pst_flow_2wk_curr_yr = DATA[(DATA.index >= strt_d8_2wk_b4) & 
                                    (DATA.index <= strt_d8_1day_b4)]
        pf_cy_2wk_MEAN = pst_flow_2wk_curr_yr['flow'].mean()
        # finding total mean of past 2 weeks from entered prediction date

        # finding selection range from 'trim_range' input from the calculated
        # past 2 week current year mean
        up_bnd_mean_flw = pf_cy_2wk_MEAN*(1+trim_range)
        low_bnd_mean_flw = pf_cy_2wk_MEAN*(1-trim_range)

        # finding past 2 weeks from 1wk prediction start date
        pst_2wk_flow_hist = DATA[(DATA.index.month == strt_d8_2wk_b4.month) & 
             (DATA.index.day >= strt_d8_2wk_b4.day) & (DATA.index.day <= strt_d8_1day_b4.day)| 
             (DATA.index.month == strt_d8_1day_b4.month) & # this part is included in case the past 2 weeks occurs between 2 months
             (DATA.index.day <= strt_d8_1day_b4.day)] 
        # all historical data in the past 2 week range found
       
        pst_2wk_hist_MEAN = pst_2wk_flow_hist.groupby(pst_2wk_flow_hist.index.year)[['flow']].mean()
        # creates average for each year for given data range

        year_selection = pst_2wk_hist_MEAN[(pst_2wk_hist_MEAN['flow'] > low_bnd_mean_flw) 
                                            & (pst_2wk_hist_MEAN['flow'] < up_bnd_mean_flw)]
        
        year_list = year_selection.index.tolist()
        # list of years that will be used for 1 week and 2 week prediction averages

        def get_mean_by_yr_from_date_range(df = DATA, predct_strt_d8 = start_date_week1_prediction, years = year_list, std_dev_mag = std_dev_size , lst_day = last_day):
                predct_strt_d8 = pd.to_datetime(predct_strt_d8)
                predct_end_date =  predct_strt_d8 + pd.DateOffset(days=6)
                strt_day = predct_strt_d8.day
                strt_month = predct_strt_d8.month
                end_day = predct_end_date.day
                end_month = predct_end_date.month

                if strt_month == end_month:
                        prdct_ds = df[((df.index.year.isin(years)) & 
                                       (df.index.month == strt_month) & 
                                       (df.index.day >= strt_day) & 
                                       (df.index.day <= end_day))]
                else:
                        prdct_ds = df[((df.index.year.isin(years))) & 
                                      ((df.index.month == strt_month) & 
                                       (df.index.day >= strt_day)) | 
                                       (df.index.month == end_month) & 
                                       (df.index.day <= end_day)]
                        
                prdct_by_yr_MEAN = prdct_ds.groupby(prdct_ds.index.year)[['flow']].mean()
                max_flow_bnd = int(prdct_by_yr_MEAN.std().iloc[0])*std_dev_mag
                max_flow_value = int((prdct_by_yr_MEAN.mean() + max_flow_bnd).iloc[0])
                trimmed_avg_flow = prdct_by_yr_MEAN[prdct_by_yr_MEAN['flow'] <= max_flow_value]
                mean_flow_trimmed = trimmed_avg_flow['flow'].mean()
                # removing outliers from 1 week and 2 week out histroical averages

                day_b4_prdct_hist_avg = df[(df.index.month == strt_month) & (df.index.day == lst_day)]['flow'].mean()
                day_b4_crrnt_yr = df[df.index == strt_d8_1day_b4]['flow'][0]
                corr_fctr = round(day_b4_crrnt_yr / day_b4_prdct_hist_avg,1)
                # using last useable day to correct for possible trends of upcoming week   

                final_prediction = round(corr_fctr*mean_flow_trimmed,1)
                return[final_prediction, mean_flow_trimmed, corr_fctr]
        
        
        wk1_crcd_prdct = get_mean_by_yr_from_date_range(predct_strt_d8 = start_date_week1_prediction)[0]
        wk2_crcd_prct = get_mean_by_yr_from_date_range(predct_strt_d8 = start_date_week2_prediction)[0]

        return[wk1_crcd_prdct,wk2_crcd_prct,DATA]
        


prdct_flow_array = find_streamflow_prediction_fromUSGS_stream()
wk1_prdct = prdct_flow_array[0]
wk2_prdct = prdct_flow_array[1]
#%%
url2 = 'https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customSingleStationReport/daily/start_of_period/640:AZ:SNTL%7Cid=%22%22%7Cname/-29,0/WTEQ::value,WTEQ::median_1991,WTEQ::pctOfMedian_1991,SNWD::value,PREC::value,PREC::median_1991,PREC::pctOfMedian_1991,TMAX::value,TMIN::value,TAVG::value'
 
data_rain = pd.read_table(url2, sep=',', skiprows=67)
data_rain.rename(columns={'Precipitation Accumulation (in) Start of Day Values': 'precip_accum'}, inplace=True)
length = int((np.shape(data_rain)[0]))
mid = int(length/2)

first_half = data_rain['precip_accum'].iloc[0:mid].mean()
sec_half = data_rain['precip_accum'].iloc[mid:length].mean()
#%%
if sec_half > first_half:
        rain_booster = (1+(sec_half-first_half))
        wk1_pred_final = round(rain_booster*wk1_prdct,1)
        wk2_pred_final = round(rain_booster*wk2_prdct,1)

        print('1 week out prediction:',wk1_pred_final,
              '2 week out prediction:', wk2_pred_final)
else:
        print('1 week out prediction:',wk1_prdct,
              '2 week out prediction:', wk2_prdct)

# %% IT PLOTS 
df = prdct_flow_array[2]
xdf = df[(df.index >= '2023-11-01')&(df.index <= '2023-11-30')]

#%%
plt.plot(data_rain['precip_accum'])
plt.title('Daily Precip Trend Nov 2023 in Verde Basin')
#%%
plt.plot(xdf['flow'])
plt.title('River Level Trend Nov 2023')
# %%
