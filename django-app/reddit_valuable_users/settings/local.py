from reddit_valuable_users.settings.core import *
import os


DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.ngrok.io', 'kdenny.pagekite.me', 'nameless-brook-44383.herokuapp.com']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../../db2.sqlite3'),
    }
}