SELECT  created_at::date as day, description, count(name)
FROM    events
WHERE   name = 'trained'
GROUP BY day, description
ORDER BY day