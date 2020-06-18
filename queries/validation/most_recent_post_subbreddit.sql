SELECT p.subreddit_id, MAX(p.created_at) as most_recent_post
FROM public.subreddits_post p
GROUP BY subreddit_id
ORDER BY most_recent_post DESC