select 
    r.from_user, 
    h.nationality,
    max(review_score) 
from airbnb_reviews r
inner join airbnb_hosts h
    on r.to_user = h.host_id
where r.from_type = 'guest'
group by 1, 2