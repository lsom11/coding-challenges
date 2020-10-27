with counts as (
    select 
        (select count(*) from fb_sms_sends where type = 'confirmation' and ds = '08-04-2020') total_confirmed,
        count(*) total_sms
    from fb_sms_sends
    where ds = '08-04-2020'
)
select (total_confirmed * 100) / total_sms as percent_confirmed from counts
