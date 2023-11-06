#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

data = pd.read_csv("DMV10_realestate.csv")
data.columns = data.columns.str.strip()  # Remove leading/trailing spaces
print(data)

data["distance"].fillna(data["distance"].mean(), inplace=True)
#data.dropna(inplace=True)   #removing rows having null values

filtered_data = data[(data['transactiondate'] >= 2013) & (data['distance'] <= 500)]    #filter based on year and distance

filtered_data = pd.get_dummies(filtered_data, columns=['stores']) #one-got encoding of cateforical variables

average_price_by_age = filtered_data.groupby('houseage')['unit_area'].mean()  #avg sale price by ppty age -- agg stats

# Example: Remove rows with extreme values in 'unit_area'
lower_bound = filtered_data['unit_area'].quantile(0.05)
upper_bound = filtered_data['unit_area'].quantile(0.95)
filtered_data = filtered_data[(filtered_data['unit_area'] >= lower_bound) & (filtered_data['unit_area'] <= upper_bound)]

# Display the processed DataFrame
print(filtered_data.head())


# In[ ]:




