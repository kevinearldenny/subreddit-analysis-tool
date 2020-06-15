import csv
from datetime import datetime
from praw_functions import get_subreddit_posts, get_user_posts
import pygsheets


date_format = '%Y-%m-%d %H:%M'
initial_sheet_name = 'Music Subreddits'

def get_initial_subreddit_list_gsheets():
    gc = pygsheets.authorize(service_file='reddit-analysis-280121-f1dd55e14bf9.json')
    ss = gc.open('Music Subreddits')
    w = ss.sheet1
    headers = w[0]
    srl = []
    for i2, row in enumerate(w):
        if i2 > 0:
            dd = {}
            for i, h in enumerate(headers):
                if h != '':
                    dd[h] = row[i]
            srl.append(dd)

    return srl

def get_initial_post_set(subreddits):
    initial_post_set = []
    srd = {}

    ### Get 50 most recent posts in each subreddit
    for sub in subreddits:
        s = sub['id'].replace("r/", "")
        srd[s.lower()] = sub
        sub_posts = get_subreddit_posts(s, 50)
        initial_post_set += sub_posts

    return initial_post_set, srd

def get_recent_posts_by_initial_authors(all_initial_authors):
    initial_author_posts = []
    for user in all_initial_authors:
        initial_author_posts += get_user_posts(user, 100)

    return initial_author_posts

def get_subreddit_counts_for_initial_authors_posts(initial_author_posts):
    subreddit_count = {}
    for p in initial_author_posts:
        sr = p['subreddit']
        if sr not in subreddit_count:
            subreddit_count[sr] = {
                'count': 1,
                'users': [p['author']]
            }
        else:
            subreddit_count[sr]['count'] += 1
            if p['author'] not in subreddit_count[sr]['users']:
                subreddit_count[sr]['users'].append(p['author'])

    return subreddit_count

def determine_top_music_subreddits():
    ### 1) Empirically create list of 50 subreddits: https://docs.google.com/spreadsheets/d/18Wvm2QRSc9GX3CiBvhMpel8LO8EhuJhQuZ6KGile8Ew/edit#gid=0
    subreddits = get_initial_subreddit_list_gsheets()

    ### 1b) Get initial post set of 2500 posts (50 most recent posts for 50 subreddits)
    initial_post_set, srd = get_initial_post_set(subreddits)


    ### 2) Get all of the distinct users who submitted posts
    all_initial_authors = list(set({v['author'] for v in initial_post_set}))

    ### 2b) Get 100 most recent posts for all contributors to initial subreddits
    initial_author_posts = get_recent_posts_by_initial_authors(all_initial_authors)


    ### 3) Get a count of post activity and distinct users by subreddit
    subreddit_count = get_subreddit_counts_for_initial_authors_posts(initial_author_posts)


    ### Export a CSV for manual review
    all_subreddits = subreddit_count.keys()
    with open("subreddit_counts.csv","w") as ofile2:
        c = csv.DictWriter(ofile2, fieldnames=['subreddit', 'category', 'in_initial_list', 'distinct_users', 'post_count'])
        c.writeheader()
        for sr in all_subreddits:
            dr = {
                'subreddit': sr,
                'post_count': subreddit_count[sr]['count'],
                'distinct_users': len(subreddit_count[sr]['users'])
            }
            srl = sr.lower()
            if srl in srd:
                dr['category'] = srd[srl]['category']
                dr['in_initial_list'] = True
            else:
                dr['category'] = '-'
                dr['in_initial_list'] = False
            c.writerow(dr)


determine_top_music_subreddits()