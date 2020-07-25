#!/usr/bin/env python
# coding: utf-8

# # Project World Bank
# 
# By Mostafa Jubayer Khan
# 
# 

# In[1]:


#Importing the Pandas & NumPy Libraries

import pandas as pd
import numpy as np
import pandas_gbq as gbq


# ### Reading the all the CSV Files

# In[2]:


df_1 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_EN.ATM.PM25.MC.ZS_DS2_en_csv_v2_1217689.csv', sep=',', header=0, skiprows=3, nrows=267)
df_1.columns

df_2 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1217511.csv', sep=',', header=0, skiprows=3, nrows=267)
df_2.columns

df_3 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_1217525.csv', sep=',', header=0, skiprows=3, nrows=267)
df_3.columns

df_4 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SE.PRM.CMPT.ZS_DS2_en_csv_v2_1217813.csv', sep=',', header=0, skiprows=3, nrows=267)
df_4.columns

df_5 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SI.POV.DDAY_DS2_en_csv_v2_1217581.csv', sep=',', header=0, skiprows=3, nrows=267)
df_5.columns

df_6 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SP.POP.1564.TO.ZS_DS2_en_csv_v2_1217810.csv', sep=',', header=0, skiprows=3, nrows=267)
df_6.columns

df_7 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/Data/API_SP.POP.TOTL_DS2_en_csv_v2_1217749.csv', sep=',', header=0, skiprows=3, nrows=267)
df_7.columns


# In[3]:


# Removing the last, unwanted "Unamed : 64" Column from all the DataFrame.

df_1=df_1.drop('Unnamed: 64' , 1)
df_1.columns

df_2=df_2.drop('Unnamed: 64' , 1)
df_2.columns

df_3=df_3.drop('Unnamed: 64' , 1)
df_3.columns

df_4=df_4.drop('Unnamed: 64' , 1)
df_4.columns

df_5=df_5.drop('Unnamed: 64' , 1)
df_5.columns

df_6=df_6.drop('Unnamed: 64' , 1)
df_6.columns

df_7=df_7.drop('Unnamed: 64' , 1)
df_7.columns


# In[4]:


df_1= df_1.melt(id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name = "year")
df_2= df_2.melt(id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name = "year")
df_3= df_3.melt(id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name = "year")
df_4= df_4.melt(id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name = "year")
df_5= df_5.melt(id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name = "year")
df_6= df_6.melt(id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name = "year")
df_7= df_7.melt(id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name = "year")


# In[5]:


# Renaming to Columns of the respective dataframes for removing extra space within the columns for uploading into the GoogLe Big Query
df_1=df_1.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})
df_2=df_2.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})
df_3=df_3.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})
df_4=df_4.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})
df_5=df_5.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})
df_6=df_6.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})
df_7=df_7.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code': 'Indicator_Code'})


# ### Uploading all the dataframes (df_1 to df_7)  into the Google BigQuery

# In[6]:


# Uploading all the 7 dataframes in to the Google Big Query
a = gbq.to_gbq(df_1, destination_table='BigQuery.df_1', project_id='commanding-air-282216', if_exists='replace')
b = gbq.to_gbq(df_2, destination_table='BigQuery.df_2', project_id='commanding-air-282216', if_exists='replace')
c = gbq.to_gbq(df_3, destination_table='BigQuery.df_3', project_id='commanding-air-282216', if_exists='replace')
d = gbq.to_gbq(df_4, destination_table='BigQuery.df_4', project_id='commanding-air-282216', if_exists='replace')
e = gbq.to_gbq(df_5, destination_table='BigQuery.df_5', project_id='commanding-air-282216', if_exists='replace')
f = gbq.to_gbq(df_6, destination_table='BigQuery.df_6', project_id='commanding-air-282216', if_exists='replace')
g = gbq.to_gbq(df_7, destination_table='BigQuery.df_7', project_id='commanding-air-282216', if_exists='replace')

df =[a,b,c,d,e,f,g]

for i in df :
#    i += 1
    pass
    print('Done Uploading into gbq')

print('Done Uploading into gbq')


# In[ ]:




