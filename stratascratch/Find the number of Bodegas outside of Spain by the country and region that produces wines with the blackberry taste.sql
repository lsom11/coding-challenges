select country, region_1 as region, count(*) from winemag_p1
where country != 'Spain'
and description ILIKE '%blackberry%'
group by 1, 2
order by 3 desc