SELECT name, weight, price, CAST(ROUND(CAST(1000*price/weight AS NUMERIC),2) AS FLOAT) AS price_per_kg
FROM Products
ORDER BY price_per_kg ASC, name ASC