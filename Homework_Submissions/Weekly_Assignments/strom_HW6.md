

# Week 6 Forecast - Method and Summary
### * To view the data in a coherent layout, view through the text editor interface and not through Preview * 

- I made this forecast by using pandas functions for the following methods. First, I found the average of the past two weeks (September 27 - October 6) of the daily flow values. Next I created a pandas df with an avg of the same chunk of dates for each year of the historical flow data all the way back to 1989. With the df of historical averaged flow values, I identified  all years that had a flow that was within +/- 40% of the average flow found for the 2023 Sep27-Oct6 average. 

- I used this list of years to find the histroical average from this chunk for the flow in the 1 week out time frame from todays submission and the historical average of the 2 week out time frame and used these values as my prediction for flow.

- My rationale for doing this method is I assume that weeks that have similar weather patterns in the timeframe leading up to the date of analysis will possibly have similar weather patterns in the proceeding week. Now that I am thinking further about this, I could have checked the standard deviations across the weeks historically to see if this assumption is valid... perhaps next time. 
  
- The range of 40% within the average calculated for 2023 may have been too large, however, not many years seemed to have similar averages, only 9 years out of the 34 years had averages that were in this range, about 25%. Perhaps I should have chosen a smaller range for more accuracy?


## Assignment Questions
Provide a summary of the data frames properties.


### What are the column names?
- ['agency_cd', 'site_no', 'datetime', 'flow', 'code', 'year', 'month', 'day']

### What is its index?
- index is the names for the columns in form of Pandas DF
  
### What data types do each of the columns have?
- site_no        int64
    - datetime      object
    - flow         float64
    - code          object
    - year           int64
    - month          int64
    - day            int64

### Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.

- count    12697.000000
- mean       352.511270
- std       1463.053479
- min         19.000000
- 25%         93.000000
- 50%        157.000000
- 75%        215.000000
- max      63400.000000
- Name: flow, dtype: float64

### Provide the same information but on a monthly basis (i.e. for all January, February, March etc). (Note: you should be able to do this with one or two lines of code)

flow
count	mean	std	min	25%	50%	75%	max
month								
1	1085.0	693.936406	2641.523855	158.0	202.000	220.0	314.00	63400.0
2	988.0	877.008097	3208.739869	136.0	199.000	238.0	612.50	61000.0
3	1085.0	1064.491244	2416.095415	97.0	180.000	378.0	1070.00	42200.0
4	1050.0	323.222857	584.313196	64.9	111.000	141.0	218.75	4690.0
5	1085.0	103.845991	49.928918	39.9	76.600	92.0	118.00	546.0
6	1050.0	65.066762	28.191344	22.1	48.325	60.0	76.00	481.0
7	1085.0	105.943871	214.174556	19.0	52.000	70.0	110.00	5270.0
8	1085.0	170.843687	288.914361	29.6	78.000	116.0	178.00	5360.0
9	1050.0	166.601810	274.594973	37.5	86.150	117.0	166.00	5590.0
10	1060.0	144.936038	111.023809	55.7	106.000	126.0	153.00	1910.0
11	1020.0	199.985294	225.677357	117.0	153.000	171.5	197.00	4600.0
12	1054.0	330.376660	1052.000260	153.0	189.000	203.0	225.00	28700.

5 highest flow values

agency_cd	site_no	datetime	flow	code	year	month	day
8582	USGS	9506000	2012-07-01	19.0	A	2012	7	1
8583	USGS	9506000	2012-07-02	20.1	A	2012	7	2
8581	USGS	9506000	2012-06-30	22.1	A	2012	6	30
8580	USGS	9506000	2012-06-29	22.5	A	2012	6	29
8584	USGS	9506000	2012-07-03	23.4	A	2012	7	3

5 lowest flow values

agency_cd	site_no	datetime	flow	code	year	month	day
8582	USGS	9506000	2012-07-01	19.0	A	2012	7	1
8583	USGS	9506000	2012-07-02	20.1	A	2012	7	2
8581	USGS	9506000	2012-06-30	22.1	A	2012	6	30
8580	USGS	9506000	2012-06-29	22.5	A	2012	6	29
8584	USGS	9506000	2012-07-03	23.4	A	2012	7	3



### Provide a list of historical dates with flows that are within 10% of your week 1 forecast value for the month of September. 

* The following values are between 90.405 and 110.495, which are the historical September flow values within 10 percent of the week 1 prediction


	agency_cd	site_no	datetime	flow	code	year	month	day
81	USGS	9506000	1989-03-23	109.0	A	1989	3	23
82	USGS	9506000	1989-03-24	99.0	A	1989	3	24
83	USGS	9506000	1989-03-25	97.0	A	1989	3	25
96	USGS	9506000	1989-04-07	110.0	A	1989	4	7
97	USGS	9506000	1989-04-08	102.0	A	1989	4	8
...	...	...	...	...	...	...	...	...
12654	USGS	9506000	2023-08-25	105.0	P	2023	8	25
12655	USGS	9506000	2023-08-26	100.0	P	2023	8	26
12666	USGS	9506000	2023-09-06	105.0	P	2023	9	6
12677	USGS	9506000	2023-09-17	98.5	P	2023	9	17
12678	USGS	9506000	2023-09-18	94.4	P	2023	9	18
1134 rows × 8 columns