select first_name, city, count(*) as total_orders, sum(order_cost) as total_cost from customers c
inner join orders o on o.cust_id = c.id
group by 1, 2
having count(*) > 3 and sum(order_cost) > 100
order by 3 desc