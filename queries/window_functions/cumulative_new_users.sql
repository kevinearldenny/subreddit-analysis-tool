SELECT subreddit, month, new_users, SUM(new_users) OVER(PARTITION BY subreddit
                                ORDER BY
                                month) AS cumulative_new_users FROM (SELECT subreddit,
       first_post_month AS month,
       COUNT(*) AS new_users
FROM
  (SELECT u.name AS user,
          s.name AS subreddit,
          MIN(date_trunc('month', p.created_at)) AS first_post_month
   FROM public.subreddits_user u
   INNER JOIN public.subreddits_post p
     ON p.author_id = u.name
   INNER JOIN public.subreddits_subreddit s
     ON p.subreddit_id = s.name
   GROUP BY u.name,
            s.name) f
GROUP BY subreddit,
month
ORDER BY subreddit ASC, month ASC) n