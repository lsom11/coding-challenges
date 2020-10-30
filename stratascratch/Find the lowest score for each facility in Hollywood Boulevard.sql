select facility_name, min(score)
from los_angeles_restaurant_health_inspections
WHERE lower(split_part(facility_address, ' ', 2)) = 'hollywood'
group by 1
order by 2 desc, 1