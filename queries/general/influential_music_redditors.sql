SELECT *
FROM
  (SELECT name,
          last_post,
          num_posts,
          total_post_score,
          top_post_score,
          avg_post_score,
          ROUND((total_post_score - top_post_score) / (num_posts - 1)) AS adj_avg_post_score,
          distinct_subreddits,
          all_subreddits
   FROM
     (SELECT u.name,
             COUNT(p.url) AS num_posts,
             SUM(p.score) AS total_post_score,
             MAX(p.created_at) AS last_post,
             string_agg(DISTINCT s.name::text, ', ') AS all_subreddits,
             COUNT(DISTINCT s.name) AS distinct_subreddits,
             MAX(p.score) AS top_post_score,
             ROUND(AVG(p.score), 0) AS avg_post_score
      FROM public.subreddits_user u
      INNER JOIN public.subreddits_post p
        ON p.author_id = u.name
      INNER JOIN public.subreddits_subreddit s
        ON p.subreddit_id = s.name
      GROUP BY u.name
      ORDER BY num_posts DESC, avg_post_score DESC) l
   WHERE num_posts > 3
   ORDER BY total_post_score DESC) o
WHERE adj_avg_post_score > 3