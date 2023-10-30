
# WEEK 9 Forecast Assignment

## Forecast Method
I generated my forecast by analyzing historical data and averages in similar month and daily timeframes. I used this years past 2 week average to then select and filter for similar patterns of flow in historical years. Using this data, I took the average and applied a correction factor. The correction factor was a value that was calculated from taking the ratio of predictions that were yielded with this method vs actual flows from previous weeks. The correction factor calculated from week 7 was used because it resulted in a relatively accurate prediction last week using this same general method. 

## Code Updates
I made the script better this week by having more organization, cleaning up unnecessary elements such as random indendents and spaces, adding notes and hash areas, building functions to reduce the amount of time code needs to be repeated for reused methods, and explaining the functions through annotation.   

## Creating Functions
I chose to build a few functions that selected chunks of rows from a dataframe given various conditions of starting and stop dates. I did this because I am constantly doing this data by date selection task in my forecast, and writting a function to do this saves alot of time. I wrote another function that can find a mean grouped by year from the same input conditions mentioned above, then another that takes in a dataframe named by a variable and finds mean grouped by year. I wrote these both because I am also doing this procedure frequently, and sometimes I have a named variable I would like to perform this on, while other times I have a date range in mind but not a defined variable from a certain dataframe. 

## Reflection on Past Week 
No questions so far. I thought recycling last weeks code, rewritting some sections to generalize chunks of codes and turn them into functions would go quick but it did not. I realized that I did not write my code last week to be of general use, it was very specific and therefore I had to chunk apart alot of variables and dissect other things that were confusingly interlinked and it ended up turning into a bit of an error puzzle for a while. In other words, I learned the importance of writting clean code in which variables can be understood and altered without too much headache. 

The one thing I struggled with this week is the decision to either write and define a new variable, or embed them into one code. The positive to defining many variables is it can be easier to read and track flow, and it makes editing/altering code easier, but all the names and trying to keep track of names that are distinct enough to use quickly became a bit difficult / annoying sometimes.