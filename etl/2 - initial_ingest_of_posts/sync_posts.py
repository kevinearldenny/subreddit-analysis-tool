import requests
import json
from pushshift_sync_historic import get_posts_for_time_period
from sync_users import create_user
from datetime import datetime
from pprint import pprint

# api_base = 'http://127.0.0.1:8000'
api_base = 'https://nameless-brook-44383.herokuapp.com'

date_format = '%Y-%m-%d %H:%M'
start_date = datetime.strptime('2020-01-01', '%Y-%m-%d')
end_date = datetime.now()

def get_subreddits():
    u = '{0}/subreddits/'.format(api_base)
    r = requests.get(u)
    j = json.loads(r.text)
    return j

def create_post(s):
    u = '{0}/posts/'.format(api_base)
    r = requests.post(u, data=s)

def cleanse_pushshift_and_create_post(all_data):
    for d in all_data:
        post_obj = {
            'title': d['title'],
            'created_at': datetime.utcfromtimestamp(d['created_utc']).strftime(date_format),
            'author': str(d['author']),
            'is_text_only': d['is_self'],
            'subreddit': str(d['subreddit']).lower(),
            'is_original_content': d['is_original_content'],
            'num_comments': d['num_comments'],
            'score': d['score'],
            'url': 'reddit.com' + d['permalink']
        }
        if 'upvote_ratio' in d:
            post_obj['upvote_ratio'] = d['upvote_ratio']
        else:
            post_obj['upvote_ratio'] = 1.0
        create_user(post_obj['author'])
        create_post(post_obj)

def sync_historic_data_for_subreddit(s):
    ### Sync all data before today
    last_day = (datetime.today()).day
    beginning_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())
    data = get_posts_for_time_period(s['name'], beginning_timestamp, end_timestamp)
    all_data = data
    while len(data) >= 500:
        # go back for more data
        last_one = data[499]
        beginning_timestamp = last_one['created_utc'] + 1
        l = datetime.fromtimestamp(beginning_timestamp).strftime('%Y-%m-%d')
        print(l)
        data = get_posts_for_time_period(sub=s['name'], beginning=beginning_timestamp, end=end_timestamp)
        all_data.extend(data)

    cleanse_pushshift_and_create_post(all_data)


def sync_all_historic_data(index=None):
    sr = get_subreddits()
    for i, s in enumerate(sr):
        if not index:
            pprint(s)
            sync_historic_data_for_subreddit(s)
        else:
            if i > index:
                print(s)
                sync_historic_data_for_subreddit(s)



index = 15
sync_all_historic_data(index)




