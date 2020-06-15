import requests
import json
from pprint import pprint

# api_base = 'http://127.0.0.1:8000'
api_base = 'https://nameless-brook-44383.herokuapp.com'



def create_user(name):
    d = {
        'name': name
    }
    u = '{0}/users/'.format(api_base)
    r = requests.post(u, data=d)

