select 
    distinct country 
from winemag_p1
where 
    country not in (select distinct country from winemag_p2)