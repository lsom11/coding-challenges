SELECT DISTINCT name, population, area
FROM world
WHERE NOT ((area <= 3000000) AND (population <= 25000000))