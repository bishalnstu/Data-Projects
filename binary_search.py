#!/usr/bin/env python
# coding: utf-8

# In[22]:


from math import *


def search_item(n,data):
    beg=0
    end=len(data)-1
    c=0

    m=int(input())

    while(beg<=end):
        mid=ceil((beg+end)/2)
        print(mid)
        if m==data[mid]:
            c=1
            break
        elif m<data[mid]:
            end=mid-1
        else :
            beg=mid+1

    if c == 0 :
        print("item not found")
    else :
        print("item found")
        


# 

# In[ ]:





# In[ ]:




