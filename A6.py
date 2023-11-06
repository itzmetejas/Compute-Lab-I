#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

csv_data = pd.read_csv('customers.csv')
excel_data = pd.read_excel('customers.xlsx', engine='openpyxl')

import json
with open('customers.json', 'r') as json_file:
    json_data = json.load(json_file)
json_data = pd.DataFrame(json_data)


print("CSV Data:")
print(csv_data.head())

print("\nExcel Data:")
print(excel_data.head())

print("\nJSON Data:")
print(json_data.head())

print("Structure and Info of CSV Data:")
print(csv_data.info())

# Check for missing values in CSV data
print("\nMissing Values in CSV Data:")
print(csv_data.isnull().sum())

# Check the structure of Excel data
print("\nStructure and Info of Excel Data:")
print(excel_data.info())

# Check for missing values in Excel data
print("\nMissing Values in Excel Data:")
print(excel_data.isnull().sum())

# Check the structure of JSON data
print("\nStructure and Info of JSON Data:")
print(json_data.info())

# Check for missing values in JSON data
print("\nMissing Values in JSON Data:")
print(json_data.isnull().sum())

csv_data.fillna(0, inplace=True)

# Remove duplicates in CSV data based on all columns
csv_data.drop_duplicates(inplace=True)

# Handling missing values in Excel data
# Replace missing values in Excel data with a default value (e.g., 0)
excel_data.fillna(0, inplace=True)

# Remove duplicates in Excel data based on specific columns (e.g., first_name and last_name)
excel_data.drop_duplicates(subset=['first_name', 'last_name'], inplace=True)

# Handling missing values in JSON data
# Replace missing values in JSON data with a default value (e.g., 0)
json_data.fillna(0, inplace=True)

# Remove duplicates in JSON data based on specific columns (e.g., first_name and last_name)
json_data.drop_duplicates(subset=['first_name', 'last_name'], inplace=True)

# Correct inconsistencies
# You may need to correct inconsistencies manually based on your domain knowledge

# Print the cleaned data
print("Cleaned CSV Data:")
print(csv_data.head())

print("\nCleaned Excel Data:")
print(excel_data.head())

print("\nCleaned JSON Data:")
print(json_data.head())

common_df = pd.concat([csv_data, excel_data, json_data], ignore_index=True)

# Optional: Reset index if needed
common_df.reset_index(drop=True, inplace=True)

# Print the unified DataFrame
print("Unified Data:")
print(common_df.head())

if not all(csv_data.columns == excel_data.columns) or not all(csv_data.columns == json_data.columns):
    print("Columns are not consistent across datasets.")
else:
    # Merge the datasets
    common_df = pd.concat([csv_data, excel_data, json_data], ignore_index=True)

    # Split a column and create new variables
    common_df['phone_area_code'] = common_df['phone'].str.extract(r'(\d+)')

    # Derive a new variable
    common_df['total_spent'] = common_df['orders'] * common_df['spent']

    # Print the transformed DataFrame
    print("Transformed Data:")
    print(common_df.head())
    
    
desc_stats = common_df.describe()

# Aggregate data by specific variables
# For example, you can group data by 'job' and calculate the total sales and average order value
agg_data = common_df.groupby('job').agg({'orders': 'sum', 'spent': 'mean'})

# Calculate total sales
total_sales = common_df['spent'].sum()

# Calculate average order value
average_order_value = common_df['spent'].mean()

# Calculate product category distribution
# Assuming you have a 'product_category' column in your DataFrame
product_distribution = common_df['job'].value_counts()

# Print the results
print("Descriptive Statistics:")
print(desc_stats)

print("\nAggregate Data by Job:")
print(agg_data)

print("\nTotal Sales: $", total_sales)

print("\nAverage Order Value: $", average_order_value)

print("\job Category Distribution:")
print(product_distribution)

import matplotlib.pyplot as plt
import seaborn as sns


# Create a bar plot to represent sales by product category
plt.figure(figsize=(10, 6))
sns.barplot(x='job', y='spent', data=common_df)
plt.title('Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Create a pie chart to represent the distribution of product categories
product_distribution = common_df['job'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(product_distribution, labels=product_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title('job Category Distribution')
plt.show()

# Create a box plot to visualize the distribution of order values
plt.figure(figsize=(8, 6))
sns.boxplot(x='job', y='spent', data=common_df)
plt.title('Order Value Distribution by Job')
plt.xlabel('Job')
plt.ylabel('Order Value')
plt.xticks(rotation=90)
plt.show()


# In[ ]:




