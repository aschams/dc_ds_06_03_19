
# coding: utf-8

# In[1]:


import numpy as np

names = ['Posie', 'Isla', 'Olivia', 'Aurora', 'Maeve', 'Cora', 'Amara',
 'Ada', 'Amelia', 'Charlotte', 'Emma', 'Ava', 'Corinne', 'Isabella', 
 'Amelia', 'Mia', 'Evelyn', 'Sophia', 'Harper', 'Milo', 'Jasper', 
 'Atticus', 'Theodore', 'Asher', 'Silas', 'Jack', 'Finn', 'Henry', 
 'Felix', 'Liam', 'Noah', 'Logan'] 


# In[2]:


np.random.randint(0,2)


# In[3]:


names2= names.copy()
while len(names2) > 1:
    half_length = len(names2) // 2
    names_to_remove = []
    for i in range(half_length):
        name1 = names2[2*i]
        name2 = names2[(2 * i) + 1]
        elim = np.random.randint(0,2)
        
        if elim: names_to_remove.append(name2)
        else: names_to_remove.append(name1)
        
    for name in names_to_remove:
        names2.remove(name)
print(names2[0])

