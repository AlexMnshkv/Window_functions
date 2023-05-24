#!/usr/bin/env python
# coding: utf-8

# In[70]:


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


# In[33]:


# df1.loc[mega['client_union_id'] ==  34734]


# In[34]:


df.date=pd.to_datetime(df.date)
df.time=pd.to_datetime(df.time, format = '%Y-%m-%d %H:%M:%S')

df1.date=pd.to_datetime(df1.date)
df1.create_date=pd.to_datetime(df1.create_date)


# In[35]:


df


# In[30]:


df1


# In[37]:


df2=df.groupby(['ad_id', 'event']).agg({'event':'count'}).rename(columns={'event':'ev_count'}).reset_index()

df2
# sns.set(
#     font_scale=2,
#     style="whitegrid",
#     rc={'figure.figsize':(20,7)}
#         )
# sns.displot(df1.view)


# In[38]:


df2=df2.pivot(index='ad_id', columns='event', values='ev_count').fillna(0)


# In[39]:


df2


# In[41]:


# посчитаем среднее количество разных рекламных событий (показы и клики) по объявлениям.
df2.view.mean()


# In[43]:


df1.view=np.log(df1.view)
df1


# In[44]:


sns.set(
    font_scale=2,
    style="whitegrid",
    rc={'figure.figsize':(20,7)}
        )
sns.displot(df1.view)


# In[45]:


df1=df.groupby(['ad_id', 'event']).agg({'event':'count'}).rename(columns={'event':'ev_count'}).reset_index()
df1
# df1.view=np.log(df1.view)


# In[46]:


# Прологарифмируем число показов, а затем построим график
df55=df1[df1.event=='view']
df55


# In[47]:


df55.ev_count=np.log(df55.ev_count)
df55
# sns.set(
#     font_scale=2,
#     style="whitegrid",
#     rc={'figure.figsize':(20,7)}
#         )
# sns.displot(df55, kde=False)


# In[48]:


sns.set(font_scale=2,
    style="whitegrid",
    rc={'figure.figsize':(20,7)}
        )
sns.displot(df55.ev_count)


# In[112]:


df


# In[51]:


df5=df[df.event=='view']
df5

# df4=df.groupby(['ad_id','date']).agg({'event':'count'}).rename(columns={'event':'ev_count'}).reset_index()
# df4


# In[52]:


# df5=df4.pivot(index='ad_id', columns='date', values='ev_count').fillna(0)
# df5
# нужно найти среднее количество показов на 1 объявление (ad_id) по дням, не учитывая объявления, у которых не было показов
df6 = df5.groupby(['ad_id','date']).agg({'event':'count'}).rename(columns={'event':'ev_count'}).reset_index()
df6


# In[53]:


#
df7 = df6.groupby(['date']).agg({'ev_count':'mean'}).reset_index()
df7


# In[54]:


df7.ev_count=df7.ev_count.rolling(2).mean()
df8 = df7
df8


# In[56]:


# Какое значение скользящего среднего получим за 6 апреля 2019 года? 
dfp=df7[df7.date=='2019-04-06']
dfp


# In[57]:


dfp.ev_count.mean().round(0)


# In[101]:


dfp.ev_count.max()


# In[60]:


# построим график значения просто среднего количества показов по дням 
sns.lineplot(df7.date, df7.ev_count)
sns.lineplot(df8.date, df8.ev_count)


# In[59]:


sns.lineplot(df8.date, df8.ev_count)


# In[61]:


df000=abs(df7-df8)
df000


# In[62]:


df8.append(df7.ev_count)


# In[63]:


df8=df8.dropna()
df8


# In[64]:


df7


# In[65]:


df9=df7-df8


# In[66]:


df9.abs


# In[71]:


# Объединим данные рекламы с данными о рекламных клиентах и найдем среднее количество дней от даты
mega=df.merge(df1, on='client_union_id' ,how= 'inner')


# In[72]:


mega


# In[76]:


mega=mega.rename(columns={'date_x':'date_event'})

mega.date_event=pd.to_datetime(df.date)
mega.time=pd.to_datetime(df.time, format = '%Y-%m-%d %H:%M:%S')

mega.date_y =pd.to_datetime(df1.date)
mega.create_date=pd.to_datetime(df1.create_date)
mega.dtypes


# In[77]:


mega['delta']=mega['date_event']-mega['create_date']


# In[78]:


mega


# In[ ]:




