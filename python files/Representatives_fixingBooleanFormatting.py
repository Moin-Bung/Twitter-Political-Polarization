#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
rep_df = pd.read_csv('representatives_updated.csv', 'representatives_updated',delimiter=',',)
user_ver = []
reply = []
retweet = []
mention = []
for i in rep_df['user_verified']:
    if i == 1:
        user_ver.append("True")
    else:
        user_ver.append("False")
rep_df = rep_df.drop(columns=['user_verified'])


# In[5]:


for i in rep_df['reply']:
    if i == 1:
        reply.append("True")
    else:
        reply.append("False")
rep_df = rep_df.drop(columns=['reply'])


# In[6]:


for i in rep_df['retweet']:
    if i == 1:
        retweet.append("True")
    else:
        retweet.append("False")
rep_df = rep_df.drop(columns=['retweet'])


# In[7]:


for i in rep_df['mention']:
    if i == 1:
        mention.append("True")
    else:
        mention.append("False")
rep_df = rep_df.drop(columns=['mention'])


# In[8]:


replen = len(rep_df.loc[0])
rep_df.insert(replen-1,"mention",mention,False)
rep_df.insert(replen-1,"retweet",retweet,False)
rep_df.insert(replen-1,"reply",reply,False)
rep_df.insert(replen-1,"user_verified",user_ver,False)
rep_df.head()


# In[9]:


rep_df.to_csv('representatives_updated_tweet_type.csv')

