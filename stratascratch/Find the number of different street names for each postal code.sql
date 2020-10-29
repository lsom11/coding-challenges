select
    business_postal_code,
    count(business_address)
from sf_restaurant_health_violations
group by 1
order by 2 desc, 1