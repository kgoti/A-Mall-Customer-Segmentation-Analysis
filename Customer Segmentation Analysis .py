#!/usr/bin/env python
# coding: utf-8

# #### Import Libraries

# In[75]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# #### Import Data 

# In[76]:


data = pd.read_excel('Mall Customer Segmentation Data.xlsx')


# #### Quick data look

# In[84]:


data.head()


# In[85]:


data.info()


# In[86]:


data.shape


# In[87]:


# Check the data if there is any null value or note
data.isnull().sum()


# In[104]:


data.describe()


# ### Exploratory Data Analysis (EDA)

# In[105]:


# Histogram / Bar Graph

gender_counts = data['Gender'].value_counts()

plt.figure(figsize=(8, 6))
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='viridis')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


# In[123]:


# Density
sns.kdeplot(data['Age'], fill=True)
plt.title('Density of Spending Score')
plt.xlabel('Spending Score')
plt.ylabel('Density')
plt.show()


# In[121]:


# Scatter Plot Distribution
plt.scatter(data['Age'], data['Annual Income (k$)'], color='green', alpha=0.5)
plt.title('Relationship between Age and Annual Income')
plt.xlabel('Age')
plt.ylabel('Annual Income')
plt.grid(True)
plt.show()


# ### Conclusion

# In[ ]:


The analysis indicates a higher presence of female customers, suggesting potential gender-specific trends. 
The density plot emphasizes a concentrated age group between 25 and 33. Additionally, the scatter plot reveals 
that individuals aged 30 to 50 generally have higher annual incomes. These insights offer valuable guidance for 
targeted marketing strategies, acknowledging demographic patterns for improved business decision-making.

