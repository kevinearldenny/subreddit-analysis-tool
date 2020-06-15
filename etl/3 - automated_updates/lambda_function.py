# -*- coding: utf-8 -*-
import json
from sync_posts import sync_all_current_data


def lambda_handler(event, context):
    # Your code goes here!
    limit = event['limit']
    stat = sync_all_current_data(limit)
    return {
        'statusCode': 200,
        'data': stat
    }
