#!/usr/bin/env python
# coding: utf-8

# # Project World Bank
# 
# By Mostafa Jubayer Khan
# 
# 

# In[2]:


#Importing the Pandas & NumPy Libraries

import pandas as pd
import numpy as np


# In[42]:


df_1 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_EN.ATM.PM25.MC.ZS_DS2_en_csv_v2_1217689.csv', header=None,sep=";")


# In[40]:


df_1.info()


# In[43]:


df_1=df_1.iloc[2:]
print(df_1)


# ### why I can't read or choose the specific column/s by the names or column respective position/s from the CSV file??

# In[51]:


df_1.columns['Country Name']


# In[48]:


final_df_1 = df_1['Country Name']


# In[8]:



df_2 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_EN.ATM.PM25.MC.ZS_DS2_en_csv_v2_1217689.csv', engine='python',header=None,sep='::')
#df_1.ilock[2:]
#df_2.columns


# In[9]:


df_3 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_1217525.csv', engine='python',header=None,sep='::')


# In[10]:


df_4 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SE.PRM.CMPT.ZS_DS2_en_csv_v2_1217813.csv', engine='python',header=None,sep='::')


# In[11]:


df_5 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SI.POV.DDAY_DS2_en_csv_v2_1217581.csv', engine='python',header=None,sep='::')


# In[12]:


df_6 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SP.POP.1564.TO.ZS_DS2_en_csv_v2_1217810.csv', engine='python',header=None,sep='::')


# In[13]:


df_7 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SP.POP.TOTL_DS2_en_csv_v2_1217749.csv', engine='python',header=None,sep='::')


# ### Nandish Can you please suggest me the solutions? I am trying to solve after watching many videos and blogs but getting helpless. Please help me

# In[ ]:





# In[ ]:




