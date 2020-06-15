SELECT * FROM (SELECT p.subreddit_id as subreddit, s.category, (date_trunc('month', p.created_at)) as month, COUNT(p.author_id) as retained
FROM public.subreddits_post p
INNER JOIN public.subreddits_subreddit s on p.subreddit_id = s.name
WHERE EXISTS (
    (SELECT
			date_trunc('month', p2.created_at) as month, p2.author_id as user, p2.subreddit_id as subreddit
		FROM
			public.subreddits_post p2
		WHERE
			p2.author_id = p.author_id AND p2.subreddit_id = p.subreddit_id AND date_trunc('month', p2.created_at) = '2020-01-01'
	))
GROUP BY subreddit, month
ORDER BY subreddit, month ASC) j WHERE month >= '2020-01-01' and month < '2020-06-01'