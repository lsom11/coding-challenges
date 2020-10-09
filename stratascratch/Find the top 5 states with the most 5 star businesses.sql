with five_star_business as (
    select * from yelp_business
    where stars >= 5
)
select state, count(distinct business_id) from five_star_business
group by 1