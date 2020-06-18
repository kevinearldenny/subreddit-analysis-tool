SELECT subreddit,
       MAX(months_ct) AS num_months,
       MIN(month) AS first_month
FROM
  (SELECT subreddit,
   month,
          COUNT(
                month) OVER(PARTITION BY subreddit
                            ORDER BY
                            month) AS months_ct,
          num_posts
   FROM
     (SELECT date_trunc('month', p.created_at) AS
      month,
             p.subreddit_id AS subreddit,
             COUNT(DISTINCT p.title) AS num_posts
      FROM public.subreddits_post p
      WHERE p.created_at >= '2020-01-01'
      GROUP BY p.subreddit_id,
      month) a
   ORDER BY subreddit,
   month) b
GROUP BY b.subreddit
ORDER BY num_months ASC