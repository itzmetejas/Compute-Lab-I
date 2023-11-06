import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("DMV12_Retail_Sales_Data.csv")

print(data.head())
print(data.info())
print(data.describe())
print(data.columns)
print(data.isnull().sum())

relevant_columns = data[['State', 'Sales', 'Shop_Category']]

region_sales = data.groupby('State')['Sales'].sum()
print(region_sales.head())

# Create a bar plot
plt.bar(data['State'], data['Sales'])
plt.xlabel('Region')
plt.ylabel('Total Sales Amount')
plt.title('Sales Distribution by Region')
plt.show()

# Create a pie chart
plt.pie(data['Sales'], labels=data['State'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
plt.title('Sales Distribution by Region')
plt.show()

# Sort the region_sales DataFrame in descending order by 'Sales' column
top_regions = data.sort_values(by='Sales', ascending=False)

# Get the top-performing region
top_region = top_regions.iloc[0]
print("Top-Performing Region: ", top_region['State'])

region_category_sales = data.groupby(['State', 'Shop_Category'])['Sales'].sum()
print(region_category_sales)

# Create the grouped bar plot
fig, ax = plt.subplots(figsize=(10, 6))

for region, group in region_category_sales.groupby('State'):
    group.plot(x='Shop_Category', y='Sales', kind='bar', ax=ax, label=region)

plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.title('Sales Amount by Region and Product Category (Grouped Bar Plot)')
plt.legend(title='Region')
plt.show()
