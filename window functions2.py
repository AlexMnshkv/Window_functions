#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.express as px

df=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_6/ads_data.csv')
df1=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_6/ads_clients_data.csv')
df1


# In[7]:


df


# In[8]:


mega=df.merge(df1, on='client_union_id', how= 'left')
mega


# In[9]:


mega.date_x=pd.to_datetime(mega.date_x)
mega.create_date=pd.to_datetime(mega.create_date)

mega['delta']=mega['date_x']-mega['create_date']

mega


# In[10]:


# mega=mega.rename(columns={'date_x':'date_event'})

# mega.date_event=pd.to_datetime(mega.date_event)
# mega.time=pd.to_datetime(mega.time, format = '%Y-%m-%d %H:%M:%S')

# mega.date_y =pd.to_datetime(mega.date_y)
# mega.create_date=pd.to_datetime(mega.create_date)


# In[11]:


# mega['delta']=(mega.date_event-mega.create_date)
# mega


# In[12]:


# mega.loc[(mega.client_union_id==9)] 


# In[13]:


mega_final=mega.groupby('client_union_id').agg({'delta':'min'}).reset_index()
mega_final


# In[14]:


# 7 вычислим конверсию из создания рекламного кабинета в запуск первой рекламы в течение не более 365 дней.


# In[15]:


mega


# In[16]:


timedelta =pd.Timedelta(365, unit='day')
timedelta


# In[23]:


pp=mega_final.loc[(mega_final['delta'] < timedelta)]
pp


# In[24]:


# mega.dropna()
pp=pp.dropna (subset=['delta'])
pp


# In[25]:


# Конверсия
x= (838/122078)*100
x


# In[26]:


#  разобъем клиентов по промежуткам от создания рекламного кабинета до запуска первого рекламного объявления.
# И определите, сколько уникальных клиентов запустили свое первое объявление в первый месяц своего существования (от 0 до 30 дней)
sp=pd.to_timedelta(['0d', '30d', '90d','180d','365d'])


# In[27]:


pp['Categorical']=pd.cut(pp['delta'], bins=sp, labels=['less than 1 month', 'more then 1 month', ' more then 3 month', 'more than 1 year'])
pp


# In[29]:


pp1 = pp.loc[(pp['Categorical'] == 'less than 1 month')]
pp1


# In[30]:


pp1.groupby('client_union_id',).agg({'Categorical':'count'})


# In[41]:


pp_bar=pp.groupby('Categorical', as_index=False).agg({'client_union_id':'nunique'}).sort_values('client_union_id', ascending = False)
pp_bar


# In[42]:


# построим барплот, на котором будут показаны категории с количеством уникальных клиентов
sns.barplot(data=pp_bar, x=pp_bar['Categorical'], y=pp_bar['client_union_id'])


# In[18]:


mega=mega.rename(columns={'date_x':'date_event'})

mega.date_event=pd.to_datetime(df.date)
mega.time=pd.to_datetime(df.time, format = '%Y-%m-%d %H:%M:%S')
mega.date_y =pd.to_datetime(df1.date)
mega.create_date=pd.to_datetime(df1.create_date)


# In[19]:


mega['delta']=mega['date_event']-mega['create_date']
mega


# In[20]:


timedelta =pd.Timedelta(365, unit='day')
timedelta


# In[21]:


pp=mega.loc[(mega['delta'] < timedelta)]
pp


# In[117]:


# Создали лк за последний год
pp_soz= pp.groupby('client_union_id').agg({'create_date':'count'}).reset_index()
pp_soz.shape


# In[118]:


# Создали лк и запустили рекламу за последний год
pp=pp.dropna (subset=['date_event'])
pp_zap= pp.groupby('client_union_id').agg({'create_date':'count'}).reset_index()
pp_zap.shape


# In[ ]:





# In[92]:


# pp=pp.dropna (subset=['date_event'])
# pp
# Дропнуть запуск рекламы


# In[107]:


pp.groupby('client_union_id').agg({'create_date':'count'}).reset_index()


# In[93]:


pp.groupby('client_union_id').agg({'campaign_union_id':'count'}).reset_index()
# Создали кабинет, но не запустили рекламу


# In[67]:


mega1 = mega.groupby('client_union_id',as_index=False).agg({'delta':'min'})
# mega1.dropna()
mega1


# In[71]:


mega1=mega1.dropna (subset=['delta'])
mega1


# In[70]:


mega1.delta.mean()


# In[ ]:


pp=pp.dropna (subset=['date_event'])


# In[72]:


mega


# In[80]:


mega.groupby('client_union_id').agg({'campaign_union_id':'count'}).reset_index()


# In[73]:


timedelta =pd.Timedelta(365, unit='day')
timedelta


# In[81]:


pp=mega.loc[(mega['delta'] < timedelta)]


# In[82]:


pp


# In[83]:


pp=pp.dropna (subset=['date_event'])
pp


# In[84]:


pp.groupby('client_union_id').agg({'campaign_union_id':'count'}).reset_index()

