select
    facility_zip,
    count(distinct facility_id) as unique_facilities,
    count(record_id) as number_of_inspections
from los_angeles_restaurant_health_inspections
group by 1
order by 3 desc