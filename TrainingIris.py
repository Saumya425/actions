#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression


# In[2]:


iris = load_iris()

X = iris.data

y = iris.target


# In[3]:


X


# In[4]:


clf = LogisticRegression()

clf.fit(X, y)


# In[9]:


pip freeze > "C:\Users\sharsaum\Downloads\actions\requirements.txt"  

