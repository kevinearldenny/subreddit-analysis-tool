# Reddit PRAW DB sync scripts

This module is run on a recurring basis and is currently deployed to AWS lambda. However,  you can run locally to test as well

## Testing locally
Requirements:
- Python 3
- pip
- virtualenv

Instructions
1) virtualenv env -p python3
2) source env/bin/activate
3) pip install -r requirements.txt
4) python sync_posts.py