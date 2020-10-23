WITH purchase_history as (
    SELECT
        user_id,
        MIN(created_at) AS first_purchase,
        MAX(created_at) as last_purchase
    FROM coin_transactions
    GROUP BY 1
)
SELECT COUNT(user_id) FROM purchase_history
WHERE last_purchase > first_purchase
