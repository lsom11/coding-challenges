SELECT zipcode, AVG(PRICE) FROM intuit_transaction
GROUP BY 1
HAVING AVG(price) > (SELECT AVG(price) FROM intuit_transaction)
ORDER BY 1 ASC