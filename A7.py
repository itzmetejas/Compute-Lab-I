#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("telecom_customer_churn.csv")

print(df.head())  
print(df.info()) 
print(df.describe())  

df.fillna(method='ffill', inplace=True)  

df.drop_duplicates(inplace=True)

df['Gender'] = df['Gender'].str.lower() 

df['TotalCharges'] = pd.to_numeric(df['Total Charges'], errors='coerce')

z_scores = (df['TotalCharges'] - df['Total Charges'].mean()) / df['Total Charges'].std()
df = df[(z_scores.abs() < 3)]

df['TenureinMonths'] = df['Tenure in Months'] * 30 
df

scaler = StandardScaler()  
df[['MonthlyCharge', 'TotalCharges', 'TenureinMonths']] = scaler.fit_transform(df[['Monthly Charge', 'Total Charges', 'Tenure in Months']])

X = df.drop('Churn Category', axis=1)      
y = df['Churn Category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

df.to_csv("Cleaned_Telecom_Customer_Churn.csv")


# In[11]:





# In[ ]:




