#!/usr/bin/env python
# coding: utf-8

# # Python Functions
# A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.
# There are two types of functions:
# 1. Built-in functions
# 2. User-defined functions
# ### Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# In[49]:


# min() - smallest value
numbers = [10, 20, 30, 40, 50]
print("Minimum:", min(numbers))


# In[50]:


# max() - largest value
numbers = [10, 20, 30, 40, 50]
print("Maximum:", max(numbers))


# In[51]:


# len() - number of elements
numbers = [10, 20, 30, 40, 50]
print("Length:", len(numbers))


# In[52]:


# sum() - total of all elements
numbers = (1,2,3,4,5)
print("Sum:",sum(numbers))


# In[53]:


# type() - type of object
numbers = (1,2,3,4,5)
print("Type of Numbers:", type(numbers))


# In[56]:


# type() - type of object
numbers = [1,2,3,4,5]
print("Type of Numbers:", type(numbers))


# In[60]:


# type() - type of object
number = "6"
print("Type of Number:", type(number))


# In[61]:


# type() - type of object
number = 6
print("Type of Number:", type(number))


# In[62]:


num = input("Enter Number:")
print(type(num))


# In[65]:


num = int(input("Enter Number:"))
print(type(num))


# In[67]:


# range() - generate a range of numbers
for i in range(3):
    print("Range value:", i)


# In[68]:


# dict() - create a dictionary
person = dict(name="Alice", age=25)
print("Dictionary:", person)


# In[69]:


Info = dict(name="Samarth",age=24)
print("Dictionary:", Info)


# In[70]:


# list() - convert to list
list_from_range = list(range(5))
print("List:", list_from_range)


# In[71]:


# tuple() - create a tuple
name = ("SAMARTH")
my_tuple = tuple(name)
print("Tuple:", my_tuple)


# In[72]:


name = input("Enter a Input:")
my_tuple = tuple(name)
print("My tuple:",my_tuple)


# In[74]:


# set() - create a set
Num = ("SAMARTH")
my_set = set(Num)
print("Set:", my_set)
#(order may vary)


# In[76]:


# print() - used to display output (used throughout above)
print("SAMARTH")


# In[26]:


a = 9
b = 8

gmean = (a*b)/(a+b)
print(gmean)


# In[27]:


c = 8
d = 7
gmean = (c*d)/(c+d)
print(gmean)


# In[28]:


def CalculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)


# In[29]:


a = 9
b = 8
CalculateGmean(a,b)


# In[30]:


CalculateGmean(c,d)


# In[31]:


a = int(input("Enter a Number of a:"))
b = int(input("Enter a Number of b:"))
CalculateGmean(a,b)
if (a>b):
    print('a is greater than b')
else:
    print('b is greater than or equal to a')


# In[41]:


def isGreater(a,b):
    if (a>b):
        print('a is greater than b')
    else:
        print('b is greater than or Equal to a')
        


# In[42]:


a = int(input("Enter a Number of a:"))
b = int(input("Enter a Number of b:"))
CalculateGmean(a,b)
isGreater(a,b)


# In[44]:





# In[ ]:





# In[ ]:




