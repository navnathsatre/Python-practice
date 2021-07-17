# Importing important libraries
from Topic_modelling import data_clean
import tweepy
import pandas as pd
import re
#import emoji
#import nltk

# set variables for keys and tokens to access the Twitter API
mykeys = open('D:\\jupyter notebook workspace\\PROJECTS\\Topic Modeling\\tweetfile.txt','r').read().splitlines()
api_key = mykeys[0]
api_key_secret = mykeys[1]
access_token = mykeys[2]
access_token_secret = mykeys[3]

auth = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret = api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# #Featching the data from twitter
# search_words="news"
# date_since="2021-07-15"
# data_until='2021-07-16'
# tweets = tweepy.Cursor(api.search,
#               q=search_words,
#               lang="en",tweet_mode='extended',
#               since=date_since,
#               until=data_until,
#               result_type="recent").pages(1)

#Featching the data from twitter
search_words="news"
date_since='2021-07-14'
data_until='2021-07-15'
tweets = tweepy.Cursor(api.search,q=search_words,lang="en",tweet_mode='extended',
                       since=date_since,until=data_until,result_type="recent").items(300)

# Iterate and print tweets
lst=[]
for tweet in tweets:
    lst.append(tweet.full_text)

print(lst)

df=pd.DataFrame({'tweet':lst})
pd.set_option("display.max_colwidth", None)
df

# make a new column to highlight retweets
df['is_retweet'] = df['tweet'].apply(lambda x: x[:2]=='RT')
df['is_retweet'].sum()  # number of retweets
df

 # number of unique retweets
df.loc[df['is_retweet']].tweet.unique().size

# 10 most repeated tweets
df.groupby(['tweet']).size().reset_index(name='counts').sort_values('counts', ascending=False).head(10)

#import numpy as np
#import matplotlib.pyplot as plt

# # number of times each tweet appears
# counts = df.groupby(['tweet']).size().reset_index(name='counts').counts

# # define bins for histogram
# my_bins = np.arange(0,counts.max()+2, 1)-0.5

# # plot histogram of tweet counts
# plt.figure()
# plt.hist(counts, bins = my_bins)
# plt.xlabels = np.arange(1,counts.max()+1, 1)
# plt.xlabel('copies of each tweet')
# plt.ylabel('frequency')
# plt.yscale('log', nonposy='clip')
# plt.show()

def find_retweeted(tweet):
    '''This function will extract the twitter handles of retweed people'''
    return re.findall('(?<=RT\s)(@[A-Za-z]+[A-Za-z0-9-_]+)', tweet)

def find_mentioned(tweet):
    '''This function will extract the twitter handles of people mentioned in the tweet'''
    return re.findall('(?<!RT\s)(@[A-Za-z]+[A-Za-z0-9-_]+)', tweet)  

def find_hashtags(tweet):
    '''This function will extract hashtags'''
    return re.findall('(#[A-Za-z]+[A-Za-z0-9-_]+)', tweet)  

# make new columns for retweeted usernames, mentioned usernames and hashtags
df['retweeted'] = df.tweet.apply(find_retweeted)
df['mentioned'] = df.tweet.apply(find_mentioned)
df['hashtags'] = df.tweet.apply(find_hashtags)

df_clean = data_clean.whole_cleaning(df)
df_clean