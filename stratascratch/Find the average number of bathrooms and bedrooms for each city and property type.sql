select city, property_type, AVG(bathrooms), AVG(bedrooms) from airbnb_search_details
group by 1, 2
order by 1