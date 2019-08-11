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

sub = raw_input("Subreddit to scrape: ")
subreddit = reddit.subreddit(sub)

with open('./csv/{}.csv'.format(sub), mode='w') as file:
    writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_NONE)
    for submission in subreddit.top(limit=200):
            writer.writerow([submission.id, submission.url])
    print("Done!")