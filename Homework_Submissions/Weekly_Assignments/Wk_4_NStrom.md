# Week 4 Discussion Assignment


###
### Grade 
3/3 
- Really nice progress from last week to this week! So glad to hear you are feeling more confident. 
- Your point about making a game plan for your code in advance is a really good one and I will try to remember to bring that up in class. 
###

Quantitative Analysis
- The quantitative analysis I applied for this assignment was first selecting all data from the given time window. For 1 wk out, I had selected data from all years from 1989-2023 of the flows between Sept 17-23 for wk 1 and Sept 24-30 for wk 2. I set outlier limits on the data of min = 50 and max = 350. This was done by generally intuition, but also confirmed by running print functions of data in these ranges and seeing that the data in these outlier ranges was usually < about 2% of data, so I removed these outliers. 
- After having python retrieve these values within the requested conditions, I took the average of each day range and found my prediction for that week.
- The analysis was very simple, but last week I struggled solely understanding the interface of Python and the commands and what not, and this week after running through the class exercises, I feel much more comfortable with being able to figure out what is going on, so more in depth methods will come now that I at least now have the base knowledge to know how to learn and approach figuring out issues through resources. 

- By looking at the histogram - One can see the concentration of the data, where the mean and common vlaues are concentrated, and the if there is skew towards a given direction. 
- From the histogram, the avg between 1 wk out and 2 wk out look concentrated around relatively the same area, except the 2wk out histogram acutally looks as though it has some further outlier data skewing tiwards the right, suggesting that perhaps later in September, there are on some years periodically higher discharge events? 

flow_data variable
- FLOW_DATA is an array - specifically a numpy array
- it is composed of also arrays within They could be understood as "lists" b/c the arrays w/in Flow_Data are 1 row x n columns but since we are using numpy they are considered arrays. These arrays have floats in them which are the individual values. 
- 12677 rows w/ 4 columns : the column is the data type -> the row is the data itself

number of times greater in Sept than weekly avg predictions
- 1 week out: prediction = 126... there were 456 daily avgs in september > this prediction: 44% of values in Sept were greater
- 2 week out: prediction = 118... there were 511 daily avgs in sept > this prediction: 49.3% of values in Sept were greater
  
Before or during 2000
- 1wk out: 224 greater: 224: 4.1 %
- 2wk out: 251 greater: 251 4.6%

There seeems to be a relative linear decrease in flow throughout the month of september, which seems to be onsistent with what is know about this season in Arizona... (moving out of the Monsoon season)

Things are coming together in class now. I now feel like I have a little bit more of an understanding, at least where I know how to relatively use the interface and which resources I can consult if I am having issues. Somethings I need to work on however are
- keeping my code organized and assigning sensical variables that I can reference back to. 
- Allowing myself more time to return to code and work on an assignment over more than one sitting
- Review a plan and think of an overall strategy before digging too deep into coding - this avoids going into the wrong direction and building something that needs to be entirely scrapped. 


