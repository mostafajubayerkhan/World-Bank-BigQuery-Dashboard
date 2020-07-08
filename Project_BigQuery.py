#!/usr/bin/env python
# coding: utf-8

# # Project World Bank
# 
# By Mostafa Jubayer Khan
# 
# 

# In[141]:


#Importing the Pandas & NumPy Libraries

import pandas as pd
import numpy as np


# ### Is this coding right for reading the CSV file okay??

# In[203]:


df_1 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_EN.ATM.PM25.MC.ZS_DS2_en_csv_v2_1217689.csv', sep=',', header=0, skiprows=3, nrows=267)


# In[204]:


print(df_1)


# In[207]:


df_1.info()


# In[205]:


df_1.columns


# In[227]:


df_1.head(5)


# In[251]:


#Chosing only past 20 years of Data

df_1_all = df_1[['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code','1999', '2000', '2001', '2002', '2003', '2004','2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013','2014', '2015', '2016', '2017', '2018', '2019']]

print(df_all)


# In[254]:


# Removing the NA's
df_1_all.replace('', np.nan)


# ### Making the years rows instead columns

# In[262]:


df_1_allYX = df_1_all.transpose()
df_1_allYX.head()


# ### Questions: 
# ### 1. what to do with all NA values?
# ### 2. If the above process is Okay for first CSV file then should I do the same process for all the nexts files?
# ### 3. Should I add I should I do with all 7 individual dataframes? (Add all in 1 or else)?
# ### Seeking your attention. 
# 
# 

# In[280]:


df_2 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1217511.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_2.columns)
df_2.head()


# In[281]:


df_3 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_1217525.csv', sep=',', header=0, skiprows=3, nrows=267)

print(df_3.columns)
df_3.head()


# In[282]:


df_4 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SE.PRM.CMPT.ZS_DS2_en_csv_v2_1217813.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_4.columns)
df_4.head()


# In[283]:


df_5 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SI.POV.DDAY_DS2_en_csv_v2_1217581.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_5.columns)
df_5.head()


# In[284]:


df_6 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SP.POP.1564.TO.ZS_DS2_en_csv_v2_1217810.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_6.columns)
df_6.head()


# In[287]:


df_7 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SP.POP.TOTL_DS2_en_csv_v2_1217749.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_7.columns)
df_7.head()


# ### Please suggest me the solutions? I am trying to solve after watching many videos and blogs but getting helpless. Please help me
