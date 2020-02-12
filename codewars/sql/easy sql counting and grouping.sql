SELECT race, COUNT(*) count FROM demographics
GROUP BY 1
ORDER BY 2 DESC