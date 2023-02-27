# Twitter-scraper
The 'Twitter Scraper' is a Data Science project you can scrape the data in the twitter which topic you want.

App link - http://localhost:8501/

#Skills take away From This Project - Python scripting, Data Collection, MongoDB, Streamlit.

#Domain - Social Media

#Problem Statement:
Today, data is scattered everywhere in the world. Especially in social media, there may be a big quantity of data on Facebook, Instagram, Youtube, Twitter, etc. This consists of pictures and films on Youtube and Instagram as compared to Facebook and Twitter. To get the real facts on Twitter, you want to scrape the data from Twitter.
You Need to Scrape the data like (date, id, url, tweet content, user,reply count, retweet count,language, source, like count etc) from twitter.

#Approach:

By using the “snscrape” Library, Scrape the twitter data from Twitter Reference.

Create a dataframe with date, id, url, tweet content, user,reply count, retweet
count,language, source, like count.

Store each collection of data into a document into Mongodb along with the
hashtag or key word we use to Scrape from twitter. eg:({“LIC
corporation+current Timestamp”: [{1000 Scraped data from past 100 days }]})

Create a GUI using streamlit that should contain the feature to enter the
keyword or Hashtag to be searched, select the date range and limit the tweet
count need to be scraped. After scraping, the data needs to be displayed in the
page and need a button to upload the data into Database and download the
data into csv and json format.

#Results: You have to build a solution that should be able to scrape the twitter data and store that in the database and allow the user to download the data with multiple data formats.
