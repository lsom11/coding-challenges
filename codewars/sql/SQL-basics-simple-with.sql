WITH special_sales AS (
  SELECT * FROM sales
  WHERE price > 90.00
)

SELECT id, name FROM departments
  WHERE id in (SELECT department_id FROM special_sales)

