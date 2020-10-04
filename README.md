# SubredditScraper
Python script using [praw](https://praw.readthedocs.io/en/latest/) to download images and gifs (as `mp4`) from any sub[reddit](https://www.reddit.com/).

## Get started
1. Create a reddit app [here](https://www.reddit.com/prefs/apps/).
2. Add <b>config.py</b> with following contents to project root directory.
<pre>
client_id='my client id'
client_secret='my client secret'
user_agent='my user agent'
username='my username'
password='my password'
</pre>
3. Run:
`pip3 install praw`

## Usage
`python3 scraper.py`

Example: To download images from 'wallpapers' subreddit. Dowloaded files are in `tmp/`

<img src="https://github.com/p1yu5h/SubredditScraper/blob/master/sample.png" />
