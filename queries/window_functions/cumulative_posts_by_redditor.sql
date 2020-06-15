SELECT author_id,
   month,
          month_posts,
          month_score,
          month_score / month_posts AS avg_month_post_score,
          SUM(month_posts) OVER(PARTITION BY author_id
                                ORDER BY
                                month) AS cumulative_post_count,
          SUM(month_score) OVER(PARTITION BY author_id
                                ORDER BY
                                month) AS running_total_post_score
   FROM
     (SELECT DATE_TRUNC('month', p1.created_at) AS
      month,
             p1.author_id,
             p1.subreddit_id,
             SUM(p1.score) AS month_score,
             COUNT(DISTINCT p1.title) AS month_posts
      FROM public.subreddits_post p1
      WHERE p1.created_at > '2020-01-01'
      GROUP BY
      month,
               p1.subreddit_id,
               p1.author_id
      ORDER BY author_id,
      month) l1