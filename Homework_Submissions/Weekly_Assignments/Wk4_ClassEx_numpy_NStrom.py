#%%
# This script contains exercises on 
# manipulating arrays with numpy
import numpy as np


# %% Exercise 1: Working with a 1-D array:
x = np.arange(0, 3**3)
print(len(x))
print(x.size)
print(x)
## 
np.size(x)
len(x)
x.size

a =np.arange(3, 45)
print(a)
a.size 

# 1.1 What is the length of x?
## 27
## x.size - attribute: coming off of the variable 

# Comprehension question is this an attribute or a method or a function of x? How do we know?

#%%
# 1.2 Get the first value out of x and print it: 
print(x[0])
print(x[26])
print(x[-1])

## use x[x.size-1] - finds last digit if dont know how big it is
print(x.size-1)
print(x.size-3)

print(x[:5])
print(x[22:])

print(x.size)

print(x[(x.size-5):])
#%%
# 1.3. Get the last value out of x and print it?

print(x[(x.size-1)]) ## last value out of x = 26

#%%
# 1.4. Get the first 5 values and last 5 values out of x and print them?
print(x[0:5]) ## first 5 values
print(x[(x.size-5):]) ## print the last 5 values 

#%%
# %% Exercise 2: Working with a 2-D array:
# 2.1 Get the first 9 values of x, and reshape them to a
#    3x3 matrix. Assign this matrix to the variable `y`
print(x[0:9])

y = np.reshape(x[0:9],(3,3))
print(y) ## y printed as a the first 9 digits in a 3x3 matrix 
## reshape is a function of y

#BONUS show how you can do this with two lines of code and how you can do it with one line of code. 

##Comprehension question: Is reshape a function, a method or an attribute of y?  How do we know? 

#%%
# 2.2 Get the middle value out of y and print it?
y = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],])

print(y[1,1]) ## middle value extracted and printed
print(y.shape)

#%%
# 2.3. Get the first row out of y and print it?
print(y[0,:]) ## printed first row 

# %%
# 2.4 If you save the first row of y to a new variable w what type of object is w? 
w = y[0,:]
print(w)
print(type(w)) ## type is "<class 'numpy.ndarray'>" --> it is an array 

#%%
# 2.5 Get the first column out of y and print the lenght of this colum? (hint you will need to use the attribute 'size' to do this)
a = (y[:,0])
print(np.size(a)) 
## ^ 2 lines of code
print(len(y[:,0])) ## both of these codes will find the length of the column 
print(np.size(y[:,0]))
## ^ one line of code x2 diff ways

# BONUS: Try doing this two different ways. First where you save the column as a new variable and then get its size (i.e. with two lines of code). And next where you combine thos commands into one line of code

#%% Exercise 3 Creating numpy arrays: 

# %%
# 3.1 use the np.arange function and the reshape method to create a numpy array with 3 rows and two columns that has values 0-9
b = np.arange(10)
bR = b.reshape((5,2)) ## I did not have the theoretical mathematical intelligence to make a 3x2 matrix w/ 10 numbers
## So made a 5x2 matrix instead 
print(bR) ## reshaped to 5x2 matrix

# %%
# 3.2 use the np.ones function to create a 4 by 4 matrix with all ones 

t = (np.ones((4,4), dtype=int)) ## added the dtype b/c I dont like the '.' 
print(t)

# %% 
# 3.3 Now modify the matrix you created in the last exercise to make the values all 4's   (Hint: you could do this with either addition or multiplication)
t *= 4 
print(t) ## they are now all 4s 

#%% Exercise 4:  using the axis argument
z=np.arange(20).reshape((5,4))
print(z)

print(np.sum(z)) ## the sum of z is 190 


# 4.1 Use 'sum' to print the total of z

#Comprehension question -- is 'sum' a function a method or an attribute?  

## np.sum is a function 

#%%
# 4.2. Print the sum along the first dimension of z?
len(z)
z.ndim
# print(z.shape)
# print(z.ndim)
# print(len(z))
## since len() returns the height of the matrix - this first dimension would be considered the rows
# print(len(z[0,:]))
# print(z)
print(sum(z[0,:])) ## sum along the "first dimension" is 6
## Comprehension question -- is the 'first dimension' the rows or the columns of z? 
# print(sum(z[:,0])) - sum of 1st column
# np.sum(z)
# %% 
# 4.3 How many elements does your answer to exercise 4.2 have? (i.e. how many numberd did you get back?)
## I got one number back because I summed a row of numbers which outputs a single value. 
# How does this compare to the shape of z? 
print(z.shape) ## z.shape outputs the dimensions of the matrix so it will give you two int. 
# the len() function will return the amount of rows present in the array / matrix 

# %%
