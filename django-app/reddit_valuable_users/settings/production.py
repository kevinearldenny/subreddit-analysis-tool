from reddit_valuable_users.settings.core import *
import os
import dj_database_url

DEBUG = True
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['nameless-brook-44383.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}