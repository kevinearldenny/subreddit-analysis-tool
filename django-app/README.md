# Subreddit Analysis tool - Django application

This Django application works to store metadata around Reddit posts for a specified set of subreddits for analysis


# Running locally

Requirements: Python 3, virtualenv
1) virtualenv env -p python3
2) source env/bin/activate
3) pip install -r requirements.txt
4) python manage.py makemigrations
5) python manage.py migrate
6) python manage.py runserver

# Ingesting data

See the etl folder for further instructions