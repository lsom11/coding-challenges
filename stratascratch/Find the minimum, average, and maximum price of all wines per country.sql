select country, min(price), avg(price), max(price) from winemag_p1
group by country
order by 1