select taster_name, variety, count(*) from winemag_p2
group by 1, 2
order by 1, 2, 3 desc