
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import datetime as dt


# In[10]:


df = pd.read_csv("co2_mm_mlo.txt", sep = r"\s*", skiprows = 72, 
                 header = None, 
                 names = ['Year', 'Month', 'Inferred_Date', 
                            'CO2_average_ppm', 'Interpolated_CO2_ppm', 'seasonal_trend',
                            'days'])


# In[12]:


df.tail()


# In[13]:


three_cols = df.iloc[:, [0, 1, 3]]


# In[14]:


three_cols.head()


# In[25]:


three_cols.iloc[0,:]


# In[26]:



for i in range(three_cols.shape[0]):
    vals = three_cols.iloc[i,:]
    if vals['CO2_average_ppm'] == -99.99: 
        three_cols.iloc[i, 2] = np.nan
        
        


# In[27]:


three_cols.head()


# In[48]:


CO2_measurements = three_cols.copy()


# In[49]:


CO2_measurements['Day'] = 15


# In[50]:


CO2_measurements.head()


# In[51]:


CO2_measurements.dtypes


# In[52]:


dt.date(int(CO2_measurements.iloc[0, :]['Year']), 
        int(CO2_measurements.iloc[0, :]['Month']), 
        int(CO2_measurements.iloc[0, :]['Day']))


# In[53]:


CO2_measurements.apply(lambda x: x['Year'], axis = 1).head()


# In[54]:


CO2_measurements['Date'] = CO2_measurements.apply(lambda x: dt.date(year = int(x['Year']), 
                                                                    month = int(x['Month']), 
                                                                    day = int(x['Day'])), 
                                                 axis = 1)


# In[55]:


CO2_measurements.head()


# In[58]:


CO2_measurements = CO2_measurements.drop('Day', axis = 1)


# In[63]:


yearly_CO2_mean = CO2_measurements.groupby(by = 'Year').mean()['CO2_average_ppm']


# We would like to select `CO_average_ppm`, `seasonal_trend` and `Date` in order to start building a model. 

# In[68]:


four_cols = df.iloc[:, [0, 1, 3, 5]].copy()
four_cols['Day'] = 15
four_cols['Date'] = four_cols.apply(lambda x: dt.date(year = int(x['Year']), 
                                                                    month = int(x['Month']), 
                                                                    day = int(x['Day'])), 
                                                 axis = 1)
four_cols = four_cols[['Date','CO2_average_ppm','seasonal_trend']]
four_cols_array = np.array(four_cols)
four_cols_array


# In[79]:


df2 = df.copy()
df2.CO2_average_ppm = np.where(df2.CO2_average_ppm == -99.99, np.nan, df2.CO2_average_ppm)
df2.head()

