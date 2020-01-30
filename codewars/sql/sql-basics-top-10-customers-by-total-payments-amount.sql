SELECT c.customer_id, c.email, COUNT(p.payment_id) as payments_count, CAST(SUM(p.amount) as float) as total_amount
FROM customer c
JOIN payment p
on p.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_amount DESC
LIMIT 10;