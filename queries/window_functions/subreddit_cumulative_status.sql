SELECT subreddit,
       category,
       month,
       num_posts_in_month,
       num_users_in_month,
       posts_per_user,
       total_post_score_in_month,
       avg_post_score,
       running_month_count,
       running_post_count,
       ROUND((running_post_count / running_month_count), 0) AS running_avg_posts_per_month,
       ROUND((num_posts_in_month - (running_post_count / running_month_count)), 0) AS post_volume_change_vs_running_avg,
       ROUND((((num_posts_in_month - (running_post_count / running_month_count)) / (running_post_count / running_month_count)) * 100), 2) AS post_volume_change_perc_vs_running_avg,
       running_total_post_score,
       ROUND((running_total_post_score / running_post_count), 2) AS running_avg_post_score,
       ROUND(avg_post_score - (running_total_post_score / running_post_count), 2) AS engagement_change_vs_running_avg
FROM
  (SELECT subreddit,
          category,
   month,
          num_posts AS num_posts_in_month,
          num_users AS num_users_in_month,
          ROUND((num_posts::decimal / num_users::decimal), 2) AS posts_per_user,
          total_post_score AS total_post_score_in_month,
          ROUND((total_post_score::decimal / num_posts::decimal), 2) AS avg_post_score,
          COUNT(
                month) OVER(PARTITION BY subreddit
                            ORDER BY
                            month) AS running_month_count,
          SUM(num_posts) OVER(PARTITION BY subreddit
                              ORDER BY
                              month) AS running_post_count,
          SUM(total_post_score) OVER(PARTITION BY subreddit
                                     ORDER BY
                                     month) AS running_total_post_score
   FROM
     (SELECT s.name AS subreddit,
             s.category,
             DATE_TRUNC('month', p.created_at) AS
      month,
             COUNT(DISTINCT p.author_id) AS num_users,
             SUM(p.score) AS total_post_score,
             COUNT(DISTINCT p.title) AS num_posts
      FROM public.subreddits_post p
      INNER JOIN public.subreddits_subreddit s
        ON p.subreddit_id = s.name
      WHERE p.created_at >= '2020-01-01'
        AND p.created_at < '2020-06-01'
      GROUP BY s.name,
      month
      ORDER BY s.name,
      month ASC) l1) l2