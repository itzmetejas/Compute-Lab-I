#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns


data = pd.read_csv("DMV11_PNQ_AQI.csv")

data.head()
data.info()
data.describe()
data

data.columns = data.columns.str.replace(' µg/m3', '')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values(by=['Date'], inplace=True, ignore_index=True)


monthly_aqi = data.resample('M', on='Date')['AQI'].mean()

# Create a line plot for AQI vs. month
plt.plot(monthly_aqi.index, monthly_aqi.values, color='b', marker='o', label='AQI (Monthly Average)')
plt.title('Monthly AQI Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Average AQI Value')
plt.grid(True)
plt.show()

# Create separate line plots for each pollutant
# PM2.5
plt.plot(data['Date'], data['SO2'], label='SO2', color='b')
plt.title('SO2 Trend Over Time')
plt.xlabel('Date')
plt.ylabel('SO2 Level')
plt.grid(True)
plt.show()

# PM10
plt.plot(data['Date'], data['Nox'], label='NOx', color='g')
plt.title('NOx Trend Over Time')
plt.xlabel('Date')
plt.ylabel('NOx Level')
plt.grid(True)
plt.show()

# CO
plt.plot(data['Date'], data['RSPM'], label='RSPM', color='r')
plt.title('RSPM Trend Over Time')
plt.xlabel('Date')
plt.ylabel('RSPM Level')
plt.grid(True)
plt.show()

# SPM
plt.plot(data['Date'], data['SPM'], label='SPM', color='y')
plt.title('SPM Trend Over Time')
plt.xlabel('Date')
plt.ylabel('SPM Level')
plt.grid(True)
plt.show()

# Create a bar plot to compare AQI values across different dates
plt.bar(data['Date'], data['AQI'], color='skyblue')
plt.title('AQI Comparison Across Dates')
plt.xlabel('Date')
plt.ylabel('AQI Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter plot of AQI vs. SO2
plt.scatter(data['SO2'], data['AQI'], alpha=0.5, color='blue')
plt.title('AQI vs. SO2 Scatter Plot')
plt.xlabel('SO2 Level')
plt.ylabel('AQI')
plt.grid(True)
plt.show()

# Scatter plot of AQI vs. NOx
plt.scatter(data['Nox'], data['AQI'], alpha=0.5, color='green')
plt.title('AQI vs. NOx Scatter Plot')
plt.xlabel('NOx Level')
plt.ylabel('AQI')
plt.grid(True)
plt.show()

# Bubble chart of AQI vs. RSPM
plt.scatter(data['RSPM'], data['AQI'], s=data['AQI'], alpha=0.5, color='red')
plt.title('AQI vs. RSPM Bubble Chart')
plt.xlabel('RSPM Level')
plt.ylabel('AQI')
plt.grid(True)
plt.show()

# Bubble chart of AQI vs. SPM
plt.scatter(data['SPM'], data['AQI'], s=data['AQI'], alpha=0.5, color='purple')
plt.title('AQI vs. SPM Bubble Chart')
plt.xlabel('SPM Level')
plt.ylabel('AQI')
plt.grid(True)
plt.show()


# In[ ]:




