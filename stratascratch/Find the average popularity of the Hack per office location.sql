select
    e.location,
    avg(popularity)
from facebook_employees e
left join facebook_hack_survey hs
    on e.id = hs.employee_id
group by 1