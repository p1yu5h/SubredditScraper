#! usr/bin/python
import praw
import pandas as pd
import datetime as dt
import config
import csv

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent,
                     username=config.username,
                     password=config.password)

subreddit = reddit.subreddit('memes')

with open('./meme_urls.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONE)
    for submission in subreddit.top(limit=200):
        writer.writerow([submission.url])