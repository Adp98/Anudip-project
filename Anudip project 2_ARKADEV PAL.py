#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install mysql-connector-python


# In[3]:


import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd

connection = mysql.connector.connect(
user='root',
password='Arka@1998',
host='localhost',
database="ecommerce"
)
# Create a cursor object to execute SQL queries
cursor = connection.cursor()
# Query data from the 'customer' table
cursor.execute('SELECT * FROM customer')
#After fetching data from the database we are storing it into Pandas DataFrame
customer_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in
cursor.description])
# Query data from the 'product' table
cursor.execute('SELECT * FROM product')
product_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in
cursor.description])
# Query data from the 'order_details' table
cursor.execute('SELECT * FROM order_details')
order_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in
cursor.description])
#printing first 5 records from each table
print(customer_data.head())
print(product_data.head())
print(order_data.head())



# In[4]:


# Identify the most frequent customers based on their order history
# Calculate the number of orders for each customer
customer_order_counts= order_data['customer_id'].value_counts()
# select the top 10 customers with the highest number of orders
top_10_customers=customer_order_counts.head(10)
# create a bar plot to visualize the number of orders for each customer
plt.figure(figsize=(10,6))
top_10_customers.plot(kind='bar', color='green')
plt.title('Top 10 customers by Number of Orders')
plt.xlabel('Customer ID')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--',alpha=0.7)
plt.tight_layout()
plt.show()


# In[5]:


# Identify the total number of customers city wise
city_counts=customer_data['city'].value_counts()
# Plotting the bar graph
plt.figure(figsize=(10,6))
city_counts.plot(kind='bar', color= 'orange')
plt.title('Total Number of Customers Citywise')
plt.xlabel('City')
plt.ylabel('Number of customers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[6]:


# Identify the most frequent customers based on their order history
# calculate the number of orders for each customer
customer_order_counts=order_data['customer_id'].value_counts()
#select the top 10 customers with the highest number of orders
top_10_customers=customer_order_counts.head(10)
# create a bar plot to visualize the number of orders for each customer
plt.figure(figsize=(10,6))
top_10_customers.plot(kind='bar', color='green')
plt.title('Top 10 customers by Number of Orders')
plt.xlabel('Customer ID')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.tight_layout()
plt.show()


# In[7]:


# Determine the total number of products available in each category
products_by_category=product_data['category'].value_counts()
# sort the categories alphabatically
products_by_category = products_by_category.sort_index()
# Plotting the column chart
plt.figure(figsize=(10,6))
plt.bar(products_by_category.index, products_by_category.values, color=plt.cm.tab20.colors)
plt.title('Total Number of products available by category')
plt.xlabel('category')
plt.ylabel('Number of products')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[8]:


# Analyze the distribution of products across sub categories
# Total number of products in category
city_counts=product_data['sub_category'].value_counts()
# plotting the bar graph
plt.figure(figsize=(10,6))
city_counts.plot(kind='bar', color='orange')
plt.title('Distribution of products across sub_category')
plt.xlabel('sub_category')
plt.ylabel('Number of products')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[9]:


# Identify products with low stock levels
# Filter products with low stock level
low_stock_products= product_data[product_data['stock']<15]
# Plotting the bar chart
plt.figure(figsize=(10,6))
low_stock_products.plot(kind='bar', x='product_name',y='stock',color='orange')
plt.title('Products with low stock levels')
plt.xlabel('Product Name')
plt.ylabel('Stock Level')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[ ]:




