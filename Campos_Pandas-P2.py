#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Import numpy
import pandas as pd


# In[4]:


#reads the .csv file and puts it in a variable
cars = pd.read_csv('cars.csv')
#displays the odd numbered collumns using a list of odd numbered columns
cars.loc[:,['Model','cyl','hp','wt','vs','gear']]


# In[5]:


#locates and displays the column of Mazda
cars.loc[cars['Model']=="Mazda RX4"]


# In[6]:


#locates the certain cyl of a Camaro Z28
cars.loc[cars['Model']=="Camaro Z28", ['cyl']]


# In[7]:


#makes a list of the given Models
lst = [ 'Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
#initialize an empty DataFrame
display = pd.DataFrame()
#Combines all the info of the Models to one dataframe
for x in lst:
    # locates the models and its properties
    temp = cars.loc[cars['Model'] == x, ['cyl','gear']]
    #Concatenates the temp array to the display array
    display = pd.concat([display, temp], axis=0)
#display the dataframe
display


# In[ ]:





# In[ ]:




