select o.order_date, o.order_details, o.order_cost, c.first_name from customers c
inner join orders o
on c.id = o.cust_id
where first_name = 'Jill' or first_name = 'Eva'
order by c.id