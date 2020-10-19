select 
    sum(case when status = 'closed' then 1 else 0 end)::numeric
        / count(*) * 100 as clsed_pct
from fb_account_status
where date = '01-10-2020'