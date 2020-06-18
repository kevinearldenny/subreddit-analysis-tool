# Subreddit Analysis tool

This repository contains the following components:
- Code for pulling recent and historical post data for a specified list of subreddits via the Reddit API and Pushshift API
- A Django project defining a DB schema for subreddit data to be stored and ingested into
- A collection of PostGRESQL queries used to analyze the data

## Process to run locally for analysis

1) Get the Django application running
2) Run the ETL script to create subreddits for analysis
3) Ingest historical posts to present date
4) Set up a chronjob to run automated_updates module

Please see the additional README.md files located in the sub-folders of this repo for the Django app (step 1) and ETL scripts (steps 2-4)