import pandas as pd
import numpy as np

#df_1 = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Nandish_IT/API_EN.ATM.PM25.MC.ZS_DS2_en_csv_v2_1217689.csv', header=None,sep=";")
dff = pd.read_csv('/Users/mostafajubayerkhan/Desktop/Education/Resume/Sabber Vai/Udemy/Python for Data Science and Machine Learning/Refactored_Py_DS_ML_Bootcamp-master/11-Linear-Regression/USA_Housing.csv')

#print(dff)

#Removing 3 Rows)
#df_2 = df_1.iloc[2:]
#df_2.head()
#print(df_2)

#df_2.head(10)

#print(dff)

dp = dff['Avg. Area Income']