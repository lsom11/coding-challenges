select
    date,
    (SUM(case
            when action = 'accepted' then 1
            else 0
    end) * 100) / count(*) as acceptance_rate
from fb_friend_requests
group by date

