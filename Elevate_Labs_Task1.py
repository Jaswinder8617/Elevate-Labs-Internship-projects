#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np

# Step 1: Create raw messy data
data = {
    'Name ': ['Alice', 'Bob', 'Charlie', 'Bob', None, 'Eve'],
    ' Age': [25, '30', 35, '30', 28, None],
    'Gender': ['F', 'male', 'Male ', 'male', 'f', 'FEMALE'],
    'Country ': ['India', 'india', 'USA', 'Usa', 'UK', 'usa'],
    'JoinDate': ['01/02/2020', '2020-03-15', '15-04-2021', '2020/03/15', None, '12.05.2022']
}

df = pd.DataFrame(data)
print("Messy Data:\n")
print(df)


# In[13]:


# Rename columns properly
df.columns = ['name', 'age', 'gender', 'country', 'joindate']

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing name or age
df = df.dropna(subset=['name', 'age'])

# Clean gender values
df['gender'] = df['gender'].str.lower().str.strip()
df['gender'] = df['gender'].replace({'f': 'female', 'female': 'female', 'male': 'male'})

# Clean country values
df['country'] = df['country'].str.lower().str.strip()

# Convert age to number
df['age'] = df['age'].astype(int)

# Convert joindate to date format
df['joindate'] = pd.to_datetime(df['joindate'], dayfirst=True, errors='coerce')

# Fill empty dates with default date
df['joindate'] = df['joindate'].fillna(pd.to_datetime('01-01-2000', dayfirst=True))

# Show cleaned data
print("\nCleaned Data:\n")
print(df)


# In[ ]:




