select c.first_name, sum(o.order_cost) from customers c
join orders o
    on c.id = o.cust_id
group by 1
order by 1
