#! usr/bin/python
import praw
from prawcore import NotFound
import config
import csv
import requests
from multiprocessing.pool import ThreadPool
import os

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password,
)

sub = raw_input("Subreddit to scrape: ")
limit = int(input("Results limit: "))

urls = []

def sub_exists(sub):
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
        return True
    except NotFound:
        print("Error: Subreddit r/{} Not Found...".format(sub))
        return False

def get_filename_from_url(url):
        # assumes that the last segment after the / represents the file name
        # if url is abc/xyz/file.txt, the file name will be file.txt
        return url[url.rfind("/") + 1:]

def get_filetype(file_name):
        if (file_name.find(".mp4") != -1):
                return "mp4"
        elif (file_name.find(".jpg") != -1 or file_name.find(".png") != -1):
                return "img"
        else: 
                return "default"

def download_url(url):
        if(url == ''): return
        file_name = get_filename_from_url(url)
        r = requests.get(url, stream=True)
        if r.status_code == requests.codes.ok:
                if (os.path.exists('./tmp/{}'.format(sub)) == False):
                        os.mkdir('./tmp/{}'.format(sub))
                        os.mkdir('./tmp/{}/img'.format(sub))
                        os.mkdir('./tmp/{}/mp4'.format(sub))
                folder = get_filetype(file_name)
                with open("./tmp/{}/{}/{}".format(sub, folder, file_name), 'wb') as f:
                        for data in r:
                                f.write(data)

if sub_exists(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.top(limit=limit):
        if (submission.url == ''):
                pass
        elif (submission.url.find(".jpg") != -1):
                urls.append(submission.url)
        elif (submission.url.find("gfycat") != -1):
                item_name = get_filename_from_url(submission.url)
                response = requests.get("https://api.gfycat.com/v1/gfycats/{}".format(item_name)).json()
                try:
                        gfycatUrl = response["gfyItem"]["mp4Url"]
                        file_name = get_filename_from_url(gfycatUrl)
                        if (os.path.exists('./tmp/{}/mp4/{}'.format(sub, file_name))):
                                print("File already exists! Skipping...")
                        else:
                                urls.append(gfycatUrl)
                                print("Added URL for download")
                except (KeyError, ValueError) as e:
                        pass
    print("Done!")

count = 0
results = ThreadPool(10).imap_unordered(download_url, urls)
for r in results:
    count+=1    
    print("Downloading: " + str(count))
