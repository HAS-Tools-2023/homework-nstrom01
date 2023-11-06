
#%%
import pandas as pd
import numpy as np
import urllib
import matplotlib.pyplot as plt
#from sklearn import datasets
#from sklearn.linear_model import LinearRegression

#%%
### Exercise 1: 
# Given the following dataframe:
data = np.random.rand(4, 5)

# Write a function and use it to calculate the mean of every colum of the dataframe
# If you have time try doing it with and without a for loop (You can either use the function inside your for loop or put a for loop inside your function)

def average_columns(my_array):
    ncol=my_array.shape[1]
    col_mean=np.zeros(5)
    for i in range(ncol):
        x = col_mean[i]= np.mean(my_array[:,i])
    return(x)

average_columns(data)

#%%

enter_numbers_here_with_commas = 54,343,234,123
some_numbers = np.asarray(enter_numbers_here_with_commas)

def take_mean(some_numbers):
    y = np.array(some_numbers)
    output = np.mean(y)
    return output 

take_mean(some_numbers)

#%%
#write a for loop that will loop over each column of data, take the mean and store in array that has a number for each column
#%% Exercise two: regression analysis
# For this exercise we will work with the
# iris dataset which is a classic and very easy
# multi-class classification dataset. 
# This dataset comes with the sklearn pacakge so we can just load it in directly. 
# It describes measurements of sepal & petal width/length for three different species of iris
iris_df = pd.read_csv('iris_df.csv', index_col='species')

#%%
# %%
# 1. How do you view the "unique" species in the `iris_df` index?
#hint use the function np.unique() and apply it to the index of the dataframe
np.unique(iris_df.index)
# %%
# 2. How do you "locate" only rows for the `versicolor` species?
#Hint use .loc to the rows that have the name 'versicolor'
iris_df.loc['versicolor']
# %%
# 3. Calculate the mean for every column of the dataframe grouped by species. 
# look back at our pandas examples Use groupby.mean
iris_df.groupby(iris_df.index).mean()
#%%
# %%
# 4. Make a scatter plot of the `sepal length (cm)` versus the `petal length (cm)` for the `versicolor`` species?
#hit first grab out just the rows you want to plot 
#Then use scatter plot function to plot the columns you want (plotting notes)

def plot_sepal_vs_petal_Length(data_frame, species_name, flower_part_1, flower_part_2 ):
    
    versicolor_iris = data_frame.loc[species_name]
    versicolor_sepal = versicolor_iris[[flower_part_1]]
    versicolor_petal = versicolor_iris[[flower_part_2]]

    xVers = versicolor_sepal
    yVers = versicolor_petal

    fig, ax = plt.subplots()
    ax.scatter(xVers, yVers, marker='.',color = 'tomato')

    ax.set_xlabel('sepal length (cm)')
    ax.set_ylabel('petal length (cm)')
    ax.set_title('Versicolor Sepal Length vs Versicolor Petal Length')

    return plt.show()


#%%

#plot_sepal_vs_petal_Length(iris_df, 'versicolor', 'sepal length (cm)', 'petal length (cm)')
# 5.  Do the same plot for `setosa` and `virginica` all on the same figure. Color them 'tomato', 'darkcyan', and 'darkviolet', respectively. (BONUS: Try to write the code so you only need to type each iris name one time)

#Repeat what you did in 4 three times

# can do name input as an array, so then species name can be a bracketed array and taken as a single input 

def plot_sepal_vs_petal_Length(data_frame, species_name_1 = 'versicolor', species_name_2 = 'setosa', species_name_3 =  'virginica', flower_part_1 = 'sepal length (cm)', flower_part_2 =  'petal length (cm)'):
    
    species_1 = data_frame.loc[species_name_1]
    x1 = species_1[[flower_part_1]]
    y1 = species_1[[flower_part_2]]

    species_2 = data_frame.loc[species_name_2]
    x2 = species_2[[flower_part_1]]
    y2 = species_2[[flower_part_2]]

    species_3 = data_frame.loc[species_name_3]
    x3 = species_3[[flower_part_1]]
    y3 = species_3[[flower_part_2]]

    fig, ax = plt.subplots()
    ax.scatter(x1, y1, label = species_name_1, marker='.',color = 'tomato')
    ax.scatter(x2, y2, label = species_name_2, marker='.',color = 'darkcyan')
    ax.scatter(x3, y3, label = species_name_3, marker='.',color = 'darkviolet')
    ax.legend()
    ax.set_xlabel('sepal length (cm)')
    ax.set_ylabel('petal length (cm)')
    ax.set_title('Sepal Length vs Petal Length')

    return plt.show()

# TEST CODE

#plot_sepal_vs_petal_Length(iris_df)
#plot_sepal_vs_petal_Length(iris_df, 'versicolor', 'setosa', 'virginica', 'sepal length (cm)', 'petal length (cm)')

#%%
# 6. Write a function that will do 'ax.scatter' for a given iris type and 
# desired color of points and use this to function to modify the code you make in 5

def plot_sepal_vs_petal_Length(data_frame, species_name, plot_color = 'red'):

    species_1 = data_frame.loc[species_name]
    x1 = species_1[['sepal length (cm)']]
    y1 = species_1[['petal length (cm)']]


    fig, ax = plt.subplots()
    ax.scatter(x1, y1, label = species_name, marker='.',color = plot_color)
    ax.legend()
    ax.set_xlabel('sepal length (cm)')
    ax.set_ylabel('petal length (cm)')
    ax.set_title('Sepal Length vs Petal Length')

    return plt.show()

plot_sepal_vs_petal_Length(iris_df, 'versicolor', plot_color = 'orange')
plot_sepal_vs_petal_Length(iris_df, 'setosa', plot_color = 'red')
plot_sepal_vs_petal_Length(iris_df, 'virginica', plot_color = 'blue')

#HINT no for loop needed, the function should have two arguments and you will call it 3 times. 
#Copy your code from #5 down here and replace your ax.scatter calls with your function. 



# %%
## Exercises for thursday's class

# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. You should do this two ways: (1) by modifying the read.table function arguments directly. (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 
#%% Method # 1 
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],index_col=['datetime'],
                              parse_dates =['datetime'])
print(data.info)
print(data.index)

#%% Method # 2 
#data['datetime'] = pd.to_datetime(data['datetime'])
#print(data.info())
#data = data.set_index('datetime')
#print(data.info)
#print(data.index)

# Exercise 2: 
#%%
#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 

daymet_df = pd.read_csv('daymet.csv', 
parse_dates =['date'], 
index_col = ['date'])
                              
print(daymet_df.info)
print(daymet_df.index)

#%%
#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 

daymet_df.shape
daymet_df.info()

daymet_df.head()
daymet_df.tail()

daymet_df[daymet_df.index.year == 2000].shape
daymet_df[daymet_df.index.year == 1992].shape
daymet_df[daymet_df.index.year == 2018].shape
daymet_df[daymet_df.index.year == 2021].shape
daymet_df[daymet_df.index.year == 2022].shape
# 8 different variables contained 
# date range spans from 09-25-1992 to 09-24-2022
# frequency of the data is daily, 365 days for 1993 to 2021, while 1992 contains 97 days of data, and 2022 contains 268 days of data

#%%
#2.3  Make a scatter plot of day length (dayl) vs maximum temperature. Fit a trend line 

def Plot_an_x_and_y(data_frame, x_col_name = 'dayl (s)', y_col_name = 'tmax (deg c)', plot_color = 'yellow'):

    plt.style.use('dark_background')
    x1 = data_frame[x_col_name]
    y1 = data_frame[y_col_name]


    fig, ax = plt.subplots()
    ax.scatter(x1, y1, marker='.',color = plot_color, s = .25)
    ax.set_xlabel(x_col_name)
    ax.set_ylabel(y_col_name)

    z = np.polyfit(x1, y1, 1)
    p = np.poly1d(z)
    plt.plot(x1,p(x1),"red")

    ax.set_title(f'{y_col_name} / {x_col_name}')

    return plt.show()

Plot_an_x_and_y(daymet_df)

#%%
#2.4 Make a plot with three lines 
# (1) average
# (2) min and 
# (3) max shortwave radiation (srad) vs the day of the year (i.e. 1-365)

# %%
# daymet_df.groupby(['day'])[['flow']].max()
# BROKEN FUNCTION >>> REPLACE W/ CODE RUNNING BELOW
def avg_min_max_plotter(data_frame, group_by = 'yday', variable_of_interest = 'srad (W/m^2)'):

    max_data = daymet_df.groupby([group_by])[[variable_of_interest]].max()
    min_data = daymet_df.groupby([group_by])[[variable_of_interest]].min()
    avg_data = daymet_df.groupby([group_by])[[variable_of_interest]].min()


    xMx = Oct_daily_MAX['day']
    yMx = Oct_daily_MAX['flow']
    xMn = Oct_daily_MIN['day']
    yMn = Oct_daily_MIN['flow']
    xAv = Oct_daily_flow['day']
    yAv = Oct_daily_flow['flow']
    
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

avg_min_max_plotter(daymet_df)
# %% Defining Variables
max_srad = daymet_df.groupby(['yday'])[['srad (W/m^2)']].max()
min_srad = daymet_df.groupby(['yday'])[['srad (W/m^2)']].min()
avg_srad = daymet_df.groupby(['yday'])[['srad (W/m^2)']].mean()

#%% working plot as line plot
fig, ax =plt.subplots()
ax.plot(max_srad['srad (W/m^2)'], marker='.',color='blue',label='max')
ax.plot(min_srad['srad (W/m^2)'], marker='.',color='red',label='min')
ax.plot(avg_srad['srad (W/m^2)'], marker='.',color='yellow',label='avg')

ax.set(title='Daily mins, max, averages of Shortwave Radiation', ylabel='W/m^2', xlabel='Day of year')
ax.legend()


# %% AS A SCATTER PLOT
fig, ax = plt.subplots()
x_axis_range = range(len(avg_srad))

ax.scatter(x_axis_range, max_srad['srad (W/m^2)'], marker='.', color='blue', label='max')
ax.scatter(x_axis_range, min_srad['srad (W/m^2)'], marker='.', color='red', label='min')
ax.scatter(x_axis_range, avg_srad['srad (W/m^2)'], marker='.', color='yellow', label='avg')

ax.set(title='Daily mins, max, averages of Shortwave Radiation', ylabel='W/m^2', xlabel='Day of year')

ax.legend()

plt.show()
# %%
