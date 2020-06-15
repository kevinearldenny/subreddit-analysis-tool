import requests
import json
import pygsheets
from pprint import pprint

api_base = 'https://nameless-brook-44383.herokuapp.com'



def create_user(name):
    d = {
        'name': name
    }
    u = '{0}/users/'.format(api_base)
    r = requests.post(u, data=d)

