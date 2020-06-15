import datetime
import requests
import json
from pprint import pprint


api_base = 'https://nameless-brook-44383.herokuapp.com'

def get_subreddits():
    u = '{0}/subreddits/'.format(api_base)
    r = requests.get(u)
    j = json.loads(r.text)
    return j

def get_posts_for_time_period(sub, beginning, end=int(datetime.datetime.now().timestamp())):
    """
    Gets posts from the given subreddit for the given time period
    :param sub: the subreddit to retrieve posts from
    :param beginning: The unix timestamp of when the posts should begin
    :param end: The unix timestamp of when the posts should end (defaults to right now)
    :return:
    """
    c = None
    print("Querying pushshift")
    url = "https://apiv2.pushshift.io/reddit/submission/search/" \
          "?subreddit={0}" \
          "&limit=500" \
          "&after={1}" \
          "&before={2}".format(sub, beginning, end)

    while not c:
        response = requests.get(url)
        try:
            resp_json = response.json()
            c = True
            return resp_json['data']
        except:
            print("trying again")


