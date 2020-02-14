SELECT COUNT(*) products, country 
FROM products
WHERE country IN ('Canada', 'United States of America')
GROUP BY 2
ORDER BY 1 DESC