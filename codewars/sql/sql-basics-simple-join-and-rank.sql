SELECT p.id, p.name, count(s.sale) as sale_count,
RANK() OVER (ORDER BY COUNT(s.sale)) as sale_Rank
FROM people p
JOIN sales s on s.people_id = p.id
GROUP BY p.id
