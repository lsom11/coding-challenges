select
    g.gender,
    AVG(r.review_score)
from airbnb_reviews r
join airbnb_guests g
on r.from_user = g.guest_id
group by 1
