
# coding: utf-8

# #### Problem 1

# In[2]:


cs_people = {'Charles': [68.3, 'Darwin'],
             'Alan': [36, 'Turing'],
             'Ada': [55, 'Lovelace'],
             'Anita': [62, 'Borg'],
             'Mark': [67, 'Fox']}
print(cs_people)


# #### Problem 2

# In[3]:


del cs_people['Mark']
print(cs_people)


# #### Problem 3

# In[4]:


cs_people['Anita'][0] = 8382.234
print(cs_people['Anita'])


# #### Problem 4

# In[6]:


ages = []
for person in cs_people:
    print(cs_people[person][1])
    ages.append(cs_people[person][0])
print(ages)
