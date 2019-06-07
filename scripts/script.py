#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
import json


# In[7]:


content=requests.get("https://api.github.com/emojis")


# In[8]:


print(content)


# In[35]:


edict = json.loads(content.text)


# In[34]:


with open("emojidata.md", "w") as efile:
    for k,v in edict.items():
        efile.write("\"#:"+ str(k) +"#:\""+" : "+"\""+":"+str(k)+":"+"\""+","+"\n")

