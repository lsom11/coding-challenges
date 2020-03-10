SELECT RANK() OVER ( ORDER BY sum(p.points) DESC) AS rank, SUM(p.points) AS total_points, COUNT(p.*) AS total_people, 
COALESCE(NULLIF(clan,''), '[no clan specified]') AS clan
FROM people p
GROUP BY p.clan
ORDER BY total_points DESC