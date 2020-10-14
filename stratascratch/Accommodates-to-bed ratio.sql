select city, AVG(accommodates / beds) from airbnb_search_details
group by 1
order by 2 desc