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


first = cars.head()
last = cars.tail()
firstlast = pd.concat([first, last])
firstlast


# In[3]:


get_ipython().system('jupyter nbconvert --to script RAYMUNDO_PA3.ipynb')


# In[ ]:




