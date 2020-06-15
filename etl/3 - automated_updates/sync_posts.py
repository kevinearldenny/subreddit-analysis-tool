import requests
import json
from praw_functions import get_subreddit_posts
from sync_users import create_user
from datetime import datetime, timedelta
from pprint import pprint

# api_base = 'http://127.0.0.1:8000'
api_base = 'https://nameless-brook-44383.herokuapp.com'
date_format = '%Y-%m-%d %H:%M'


def get_subreddits():
    u = '{0}/subreddits/'.format(api_base)
    r = requests.get(u)
    j = json.loads(r.text)
    return j


def create_post(s):
    u = '{0}/posts/'.format(api_base)
    r = requests.post(u, data=s)
    if r.status_code != 201:
        print(r.text)
        return 'failed'
    else:
        return 'created'


def sync_current_data_for_subreddit(s, limit):
    ct = {
        'created': 0,
        'failed': 0
    }
    pt = get_subreddit_posts(s['name'], 10)
    for p in pt:
        status = create_post(p)
        ct[status] += 1

    return ct


def sync_all_current_data(limit):
    ct = {
        'created': 0,
        'failed': 0
    }
    sr = get_subreddits()
    for s in sr:
        stat = sync_current_data_for_subreddit(s, limit)
        ct['created'] += stat['created']
        ct['failed'] += stat['failed']

    return ct





