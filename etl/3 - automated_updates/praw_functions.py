import praw
from pprint import pprint
import csv
from datetime import datetime, timezone, timedelta
from sync_users import create_user


client_id = 'VMK_fGV_LqSScA'
client_secret = 'a7AEpK_9YqC5Z4wCeYgIV0C_P3c'
user_agent = "MusicUserValue/0.1 by earldeezy"

date_format = '%Y-%m-%d %H:%M'

r = praw.Reddit(user_agent=user_agent, client_id=client_id, client_secret=client_secret)



def process_posts(post_list):
    soo = []
    for submission in post_list:
        ### Exclude comments on posts - only looking at top-level submissions
        if submission.author and hasattr(submission, 'title'):
            sub_obj = {
                'title': submission.title,
                'created_at': datetime.utcfromtimestamp(submission.created_utc).strftime(date_format),
                'author': str(submission.author.name),
                'is_text_only': submission.is_self,
                'subreddit': str(submission.subreddit.display_name).lower(),
                'is_original_content': submission.is_original_content,
                'num_comments': submission.num_comments,
                'score': submission.score,
                'upvote_ratio': submission.upvote_ratio,
                'url': 'reddit.com' + submission.permalink
            }
            create_user(sub_obj['author'])
            soo.append(sub_obj)
    return soo

def get_subreddit_posts(s, limit):
    post_list = r.subreddit(s).new(limit=limit)
    soo = process_posts(post_list)
    return soo


def get_user_posts(a, limit):
    user_posts = r.redditor(a).new(limit=limit)
    soo = process_posts(user_posts)
    return soo