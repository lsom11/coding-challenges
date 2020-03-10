SELECT p.id, p.name, count(t.*) as toy_count
from people p
left join toys t on p.id = t.people_id
group by p.id