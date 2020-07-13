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


# ### Reading the CSV File no 1

# In[3]:


df_1 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_EN.ATM.PM25.MC.ZS_DS2_en_csv_v2_1217689.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_1)


# In[4]:


# Reading all the columns head
df_1.columns


# In[5]:


# Removing the last, unwanted "Unamed : 64" Column from the DataFrame.
df_1=df_1.drop('Unnamed: 64' , 1)
df_1.columns


# In[6]:


df_1 = df_1.melt(id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name = "year")

df_1.head()


# In[7]:


df_1


# In[8]:


df_1.columns


# In[9]:


df_1=df_1.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})


# In[10]:



print(df_1)


# ### Uploading the Data Frame(df_1) into the Google BigQuery 

# In[12]:


import pandas_gbq as gbq

gbq.to_gbq(df_1, destination_table= 'World_Bank.df_1', project_id='commanding-air-282216', if_exists='replace')


# ### Reading the CSV File no 2
# 

# In[13]:


df_2 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1217511.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_2)
df_2.columns


# In[14]:


df_2 = df_2.drop('Unnamed: 64', 1)


# In[15]:


df_2.columns


# In[16]:


df_2 = df_2.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name ="Year")


# In[17]:


df_2


# ### Renaming the column to remove extra space in betweeen the columns of the dataframe for uploading into the Google BigQuery Table

# In[18]:


df_2=df_2.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})


# In[19]:


df_2


# ### Uploading the Data Frame(df_2) into the Google BigQuery 

# In[20]:


#importing the Pandas Google BigQuery Library

import pandas_gbq as gbq

gbq.to_gbq(df_2, destination_table='World_Bank.df_2', project_id='commanding-air-282216', if_exists='replace')


# ### Reading the CSV File no 3

# In[21]:


df_3 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_1217525.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_3)
df_3.columns


# In[22]:


# removing the Unnamed last Coulmn
df_3 = df_3.drop('Unnamed: 64', 1)


# In[23]:


df_3.columns


# In[24]:


# creating the years into a separate coulmn into the dataframe
df_3 = df_3.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name ="Year")


# In[25]:


df_3


# ### Renaming the column to remove extra space in betweeen the columns of the dataframe for uploading into the Google BigQuery Table

# In[26]:


df_3=df_3.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})


# ### Uploading the Dataframe (df_3) into the Google Big Query

# In[28]:


#importing the Pandas Google BigQuery Library

import pandas_gbq as gbq

gbq.to_gbq(df_3, destination_table='World_Bank.df_3', project_id='commanding-air-282216', if_exists='replace')


# ### Reading the CSV File no 4

# In[29]:


df_4 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SE.PRM.CMPT.ZS_DS2_en_csv_v2_1217813.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_4)
df_4.columns


# In[30]:


#Removing the Last Column 
df_4 = df_4.drop('Unnamed: 64', 1)


# In[31]:


df_4.columns


# In[32]:


# Renaming the "years" into a separate column
df_4 = df_4.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name ="Year")


# In[33]:


df_4


# ### Renaming the column to remove extra space in betweeen the columns of the dataframe for uploading into the Google BigQuery Table

# In[34]:


df_4=df_4.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})


# In[35]:


df_4


# In[37]:


#importing the Pandas Google BigQuery Library

import pandas_gbq as gbq

gbq.to_gbq(df_4, destination_table='World_Bank.df_4', project_id='commanding-air-282216', if_exists='replace')


# ### Reading the CSV File no 5

# In[38]:


df_5 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SI.POV.DDAY_DS2_en_csv_v2_1217581.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_5)
df_5.columns


# In[39]:


df_5 = df_5.drop('Unnamed: 64', 1)


# In[40]:


df_5.columns


# In[41]:


df_5 = df_5.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name ="Year")


# In[42]:


df_5


# ### Renaming the column to remove extra space in betweeen the columns of the dataframe for uploading into the Google BigQuery Table

# In[43]:


df_5=df_5.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})


# In[44]:


df_5


# In[45]:


#importing the Pandas Google BigQuery Library

import pandas_gbq as gbq

gbq.to_gbq(df_5, destination_table='World_Bank.df_5', project_id='commanding-air-282216', if_exists='replace')


# ### Reading the CSV File no 6

# In[46]:


df_6 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SP.POP.1564.TO.ZS_DS2_en_csv_v2_1217810.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_6)
df_6.columns


# In[47]:


df_6 = df_6.drop('Unnamed: 64', 1)


# In[48]:


df_6.columns


# In[49]:


# Removing the years into columns
df_6 = df_6.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name ="Year")


# In[50]:


df_6


# ### Renaming the column to remove extra space in betweeen the columns of the dataframe for uploading into the Google BigQuery Table

# In[51]:


df_6=df_6.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})


# In[52]:


#importing the Pandas Google BigQuery Library

import pandas_gbq as gbq

gbq.to_gbq(df_6, destination_table='World_Bank.df_6', project_id='commanding-air-282216', if_exists='replace')


# In[ ]:





# ### Reading the CSV File no 7

# In[53]:


df_7 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SP.POP.TOTL_DS2_en_csv_v2_1217749.csv', sep=',', header=0, skiprows=3, nrows=267)
print(df_7)
df_7.columns


# In[54]:


df_7 = df_7.drop('Unnamed: 64', 1)


# In[55]:


df_7.columns


# In[56]:


df_7 = df_7.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name ="Year")


# In[57]:


df_7


# In[58]:


#Renaming the years into a separete column
df_7=df_7.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})


# In[59]:


df_7


# ### Uploading all the dataframe (df_7)  into the Google BigQuery

# In[60]:


#importing the Pandas Google BigQuery Library 

import pandas_gbq as gbq

gbq.to_gbq(df_7, destination_table='World_Bank.df_7', project_id='commanding-air-282216', if_exists='replace')


# In[61]:


df_7.columns


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Reading data from Google BigQuery

# ### Example

# In[64]:


Query="""SELECT Country_name, Country_code FROM `commanding-air-282216.World_Bank.df_1` LIMIT 100"""

World_Bank_1=gbq.read_gbq(Query, project_id ="commanding-air-282216")

World_Bank_1.head(100)


# ### Please Check the Dataframe (df_1 to df_7)  and let me know the possible sugguestiosn for the Creating the dashaboards. Thanks

# In[ ]:




