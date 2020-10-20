with sent_messages as (
    select 
        user1 as user,
        SUM(msg_count) as msg_count 
    from fb_messages
    GROUP BY user1
),
received_messages as (
    select 
        user2 as user,
        SUM(msg_count) as msg_count 
    from fb_messages
    GROUP BY user2
)
select 
    sm.user, 
    COALESCE(sm.msg_count, 0) + COALESCE(rm.msg_count, 0) as msg_count
from sent_messages sm
left join received_messages rm
    on sm.user = rm.user
order by 2 desc
limit 10