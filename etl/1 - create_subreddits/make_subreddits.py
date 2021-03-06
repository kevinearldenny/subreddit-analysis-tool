import requests
import json
import pygsheets
from pprint import pprint
import csv

# api_base = 'https://nameless-brook-44383.herokuapp.com'

### Switch to this if you want to build a test DB locally
api_base = 'http://127.0.0.1:8000'


### This should be a path to your Google Service Account File
service_file_path = '<YOUR PATH HERE>'

### This should be the name of a Google Sheet
### Sheet should contain the following fields: 'name', 'url', 'category', 'in_initial_target_list'
### Example sheet: https://docs.google.com/spreadsheets/d/1bnZgLHcLCFr2bx0jmTuGWGg37cPAqyRdkIPYXad-Nbg/edit?usp=sharing
google_sheet_name = 'Subreddit Counts'

def create_user(name):
    d = {
        'name': name
    }
    u = '{0}/users/'.format(api_base)
    r = requests.post(u, data=d)
    if r.status_code != 200:
        print(r.text)

def create_subreddit(s):
    u = '{0}/subreddits/'.format(api_base)
    r = requests.post(u, data=s)
    if r.status_code != 200:
        print(r.text)

def make_subreddits_from_gsheet():
    gc = pygsheets.authorize(service_file=service_file_path)
    ss = gc.open(google_sheet_name)
    w = ss.sheet1
    headers = w[0]
    stages = {}
    nm = []
    for i2, row in enumerate(w):
        if i2 > 0:
            dd = {}
            for i, h in enumerate(headers):
                if h != '':
                    dd[h] = row[i]
            if dd['keep'] == 'Y':
                sr = {
                    'name': dd['subreddit'].lower(),
                    'url': 'https://www.reddit.com/r/{0}'.format(dd['subreddit'].lower()),
                    'category': dd['category'],
                    'in_initial_target_list': dd['in_initial_list']
                }
                create_subreddit(sr)

def make_subreddits_from_csv():
    with open("subreddits.csv","r") as ifile:
        c = csv.DictReader(ifile)
        for row in c:
            if row['keep'] == 'Y':
                sr = {
                    'name': row['subreddit'].lower(),
                    'url': 'https://www.reddit.com/r/{0}'.format(row['subreddit'].lower()),
                    'category': row['category'],
                    'in_initial_target_list': row['in_initial_list']
                }
                create_subreddit(sr)


# make_subreddits_from_gsheet()
make_subreddits_from_csv()
