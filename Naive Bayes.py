
# coding: utf-8

# In[23]:


import pandas as pd


# In[24]:


df = pd.read_csv("dataset.csv")


# In[25]:


print(df)


# In[26]:


total_rows = df.shape[0]


# In[27]:


d = {}
col = list(df.columns)


# In[28]:


#Calculating the unique value 
for c in col:
    x = list(df[c].unique())
    d[c] = x
table = {}    


# In[29]:


for c in col:
    temp = {}
    y = {}
    for i in d[col[len(col)-1]]:
        y[i] = 0
    if(c.lower()!=col[len(col)-1].lower()):
        for v in d[c]:
            x = {}
            for i in d[col[len(col)-1]]:
                value = df[(df[c]==v) & (df[col[len(col)-1]]==i)].count()
                x[i] = list([value[c]])
                y[i] = y[i] + x[i][0] 
            temp[v] = x
        for v in d[c]:
            for i in d[col[len(col)-1]]:
                temp[v][i].append(temp[v][i][0]/y[i])
        table[c] = temp    
        
        
    else:
        for v in d[c]:
            value = list(df[c]).count(v)
            prob1 = value/total_rows
            temp[v] = list([value,prob1])
        table[c] = temp    
         
        
    
        


# In[30]:


print(table)


# In[11]:


print("Testing")


# In[13]:


inputs = {}
for i in range(len(col)-1):
    inputs[col[i]] = input(col[i]+":")


# In[50]:


prob = {}
for j in d[col[len(col)-1]]:
    pr = 1
    for i in range(len(col)-1):
        pr = pr * table[col[i]][inputs[col[i]]][j][1]
        
    prob[j] = pr    
        
    


# In[51]:


prob1 = 1
for i in range(len(col)-1):
    s = 0
    for j in d[col[len(col)-1]]:
        s = s + table[col[i]][inputs[col[i]]][j][0]
    prob1 = prob1 * (s/total_rows)
        


# In[52]:


final_prob = {}
for j in d[col[len(col)-1]]:
    pr = (prob[j]*table[col[len(col)-1]][j][1])/prob1
    final_prob[j] = pr
    


# In[53]:


final_prob


# In[54]:


maximum = -99
for i in d[col[len(col)-1]]:
    if(final_prob[i]>maximum):
        maximum = final_prob[i]
        s1 = i
print("Output->",s1+":",maximum)        
        

