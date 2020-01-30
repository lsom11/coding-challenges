CREATE OR REPLACE VIEW members_approved_for_voucher AS
  WITH mbyd AS (
    SELECT s.department_id, SUM(p.price) FROM sales s
    JOIN products p ON s.product_id = p.id
    GROUP BY s.department_id
    HAVING SUM(p.price) > 10000
  )

SELECT s.member_id AS id, m.name, m.email, SUM(p.price) AS total_spending FROM sales s
LEFT JOIN products p ON s.product_id = p.id
LEFT JOIN members m ON s.member_id = m.id
WHERE s.department_id IN (SELECT department_id FROM mbyd)
GROUP BY (s.member_id, m.name, m.email)
HAVING SUM(p.price) > 1000
ORDER BY s.member_id ASC;
  
SELECT id, name, email, total_spending FROM members_approved_for_voucher