with total_searches as (
    select
        c.id_guest,
        count(s.*) as total_searches,
        SUM
            (CASE
                when ts_booking_at is not null then 1 else 0
            END
        ) as total_bookings 
    from airbnb_contacts c
    join airbnb_searches s
        on c.id_guest = s.id_user
    group by 1
)
select 
    c.id_guest,
    total_searches,
    total_bookings,
    CASE
        WHEN
            total_bookings > total_searches / 2
            THEN 'books'
        ELSE 'does not book'
    END as action,
    total_bookings / total_searches as searches_per_action
from airbnb_contacts c
join airbnb_searches s
    on c.id_guest = s.id_user
join total_searches t
    on c.id_guest = t.id_guest
group by 1, 2, 3