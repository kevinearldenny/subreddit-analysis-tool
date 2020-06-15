SELECT url,
       post_date,
       subreddit_id,
       post_score,
       l1.author_id,
       distinct_user_subreddits,
       running_post_count,
       running_total_post_score,
       (running_total_post_score / running_post_count) AS running_avg_post_score,
       all_user_subreddits
FROM
  (SELECT p1.url,
          p1.created_at AS post_date,
          p1.subreddit_id,
          p1.score AS post_score,
          p1.author_id,
          COUNT(p1.url) OVER(PARTITION BY p1.author_id
                             ORDER BY p1.created_at) AS running_post_count,
          SUM(p1.score) OVER(PARTITION BY p1.author_id
                             ORDER BY p1.created_at) AS running_total_post_score
   FROM public.subreddits_post p1
   WHERE p1.created_at > '2020-01-01'
     AND p1.score > 3
   ORDER BY p1.created_at DESC) l1
INNER JOIN
  (SELECT author_id,
          string_agg(DISTINCT subreddit_id::text, ', ') AS all_user_subreddits,
          COUNT(DISTINCT subreddit_id) AS distinct_user_subreddits
   FROM public.subreddits_post
   GROUP BY author_id) l2
  ON l1.author_id = l2.author_id
WHERE (running_total_post_score / running_post_count) > 3
  AND running_post_count > 1
  AND distinct_user_subreddits > 1
ORDER BY post_date DESC