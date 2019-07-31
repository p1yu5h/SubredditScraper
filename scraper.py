#! usr/bin/python
import praw
import pandas as pd
import datetime as dt
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent,
                     username=config.username,
                     password=config.password)

subreddit = reddit.subreddit('memes')

for submission in subreddit.top(limit=100):
    print(submission.url)




