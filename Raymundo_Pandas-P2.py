#!/usr/bin/env python
# coding: utf-8

# Johann Raymundo

# 2ECE-B

# Programming Assignment 3

# In[4]:


#access pandas library
import pandas as pd


# In[5]:


#access csv file
cars=pd.read_csv('cars.csv')


# problem 1

# In[7]:


#display the first and last 5 rows of the csv
first = cars.head()
last = cars.tail()
firstlast = pd.concat([first, last])
firstlast


# Problem 2

# In[15]:


# display first 5 rows of the database with odd-numbered column 
odd = cars.iloc[[1,3,5,7,9],: ]
odd


# In[17]:


#Display the row that contains the ‘Model’ of ‘Mazda RX4’
cars.loc[cars['Model'] == 'Mazda RX4']


# In[19]:


#Amount of cylinders (‘cyl’) the ‘Camaro Z28’ has
cars.loc[cars['Model'] == 'Camaro Z28',['cyl']]


# In[8]:


get_ipython().system('jupyter nbconvert --to script RAYMUNDO_PA3.ipynb')


# In[ ]:




