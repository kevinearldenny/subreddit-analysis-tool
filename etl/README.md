# Subreddit Analysis tool - ETL scripts

These 4 ETL modules work in conjuction with the Django application contained within this repo to populate a SQL database with metadata around Reddit posts within a specified set of subreddits


## Running locally

If you wish to run any of these modules locally, it is recommended to create a virtual environment for managing Python dependencies like so:

- virtualenv env -p python3
- source env/bin/activate
- pip install -r requirements.txt

# 0) Pre-processing

I initially started my analysis with a set of 50 subreddits that I am currently subscribed to that have content that is relevant for musicians, music producers and other music hobbyists. However, I realized that perhaps there are other music subreddits that would be worthwhile of adding into this analysis.
To create a more pertinent list of 50 music subreddits, I got the 50 most recent posts for the initial list of 50 subreddits ('initial post set'), and then queried the 100 most recent posts by each author within the initial post set, then summed up the total recent post activity and distinct users by subreddit.
The initial 50 subreddits I identified can be seen in music_subreddits.csv, and the results of this analysis step can be seen at https://docs.google.com/spreadsheets/d/1bnZgLHcLCFr2bx0jmTuGWGg37cPAqyRdkIPYXad-Nbg/edit?usp=sharing

This step can be skipped if you are confident in your initial selection of subreddits!

# 1) Create subreddits

To generate records in the DB for each subreddit, you will need a list of subreddits in a CSV mirroring the structure in this folder.
Once you have this, you can run `python make_subreddits.py` within this folder

# 2) Sync initial posts

Once you have DB records created for each subreddit you wish to sync data and analyze, the endpoint 'subreddits/' will now return a list of all subreddits in the DB, allowing for automated ingestion of post metadata into the DB for each subreddit. By default, data is synced from the beginning of 2020 to the present date

To run this module: `python sync_posts.py`

# 3) Sync posts (ongoing)

If you wish to keep data on subreddits up to date, you can set up a chronjob or AWS lambda function to run `sync_posts.py` in this folder to sync the most recent posts for each subreddit.
For the instance I have hosted on Heroku, I currently have this deployed as an AWS lambda function that is running 1x per hour.
