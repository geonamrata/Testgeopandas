#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


# #### Now you are ready to start!

# In[30]:



url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')
chipo.head(10)


# In[31]:


chipo.shape


# In[32]:


chipo.info()


# In[47]:


pd.set_option('display.max_column',5)


# In[50]:


x= chipo.item_name
x


# In[71]:


letter_counts= Counter(x)
df= pd.DataFrame.from_dict(letter_counts, orient= 'index')
df= df[0].sort_values(ascending= True)[45:50]
df.plot(kind= 'bar')
plt.xlabel('Items')
plt.ylabel("Number of Times Orders")
plt.title("Most ordered Chipotle\'s Items")
plt.show()


# In[ ]:




