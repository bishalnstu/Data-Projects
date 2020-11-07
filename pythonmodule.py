#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[29]:


str1="bishal"
str2=" biswas"
print(str1+ str2)

str3='bishal'

print(str3)


# In[3]:

# In[4]:


sparse_mat=sparse.csr_matrix(eye)
print("\nscipy martrix:\n{}".format(sparse_mat))


# In[5]:


var=int(input("input number"))
print(var)
type(var)


# In[ ]:





# In[ ]:





# In[1]:


str1='hello world'
print(len(str1))


# In[4]:


print(str1.count('l',0,len(str1)))


# In[ ]:


def checkvar(var):
    print(var.count('l',0,len(var)))   


# In[ ]:


def sumvar(a,b):
    print(a+b)


# In[30]:


def seqsum(a,b):
    sum1=(b*(b+1))/2
    sum2=(a*(a+1))/2
    sum3=sum1-sum2
    i=0
    for i in range(5,6):
        print(i)
        
    k=0
    while(k<6):
        print(k)
        k+=1
    if(sum3%2):
        return "even"
    else:
        return "odd"


# In[ ]:




