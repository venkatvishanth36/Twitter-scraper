# Import the all necessary libraries

import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo
import streamlit as st
import json
import csv

# Establishing connection with mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")
# creating database and collection to store data
db = client["Tweets_data"]
col = db.Scrape_data

# GUI interface
st.header("Twitter Data Scraper ")
limit = st.number_input("Enter Number of Data (You Want to Scrape)")
query = st.text_input("Enter a Twitter Keywords (You want to Scrape)")


tweets = [] # list to store scraped data
cols = ['Date', 'Id', 'URL', 'tweet_content', 'Reply_count', 'Retweet_count', 'Language', 'Source', 'Like_count']

st.header("Hit the Button to Scrape Data")

# below code will scrape data from twitter
if st.button("Scrape"):
    def tweet_scraper(limit, query):
        for tweet in sntwitter.TwitterSearchScraper("Query" + ' since:2023-01-01 lang:pt').get_items():
            if len(tweets) == limit:
                break
            else:
                tweets.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])
        df = pd.DataFrame(tweets, columns=cols)
        data = df.to_dict(orient="Records")
        db.Scrape_data.insert_many(data)
        st.subheader("Scraped Data")

    tweet_scraper(limit,query)

df = pd.DataFrame(tweets, columns=cols)
# scraped data will be displayed
if st.checkbox("Show_Data"):
    st.subheader('Data')
    st.write(df)

# fetching the data from mongodb and converting into Dataframe
cursor = col.find()
cursor_list = list(cursor)
df = pd.DataFrame(cursor_list)

st.header("Download the Data")
# number of data need to be downloaded is selected and displayed
no_of_datas = st.slider("Select Max_Data ", 10, 1000, 10000,step=1)
df = df.head(no_of_datas)
if st.checkbox('Data is Ready'):
    st.subheader("Downloaded Data")
    st.write(df)

# data is downloaded in JSON format
if st.button("Download JSON"):
    json = df.to_json(orient='Records',lines=True,default_handler=str)
    with open('temp.json', 'w') as f:
        f.write(json)
if st.checkbox("Display"):
    with open('temp.json', 'r') as f:
        st.write(f.read())

# data is downloaded in csv format
if st.button("Download csv"):
    csv = df.to_csv()
    with open('temp1.csv', 'w', encoding='utf-8') as f:
        f.write(csv)
if st.checkbox("Display."):
    with open('temp1.csv', 'r') as f:
        st.write(f.read())