with top_pair as (
  select a1.actor_id as id1, a2.actor_id as id2
  from film_actor a1
    inner join film_actor a2 on a1.film_id=a2.film_id
  where a1.actor_id <> a2.actor_id
  group by a1.actor_id, a2.actor_id
  order by count(a1.film_id) desc
  limit 1
)
select
(select first_name || ' ' || last_name from actor where actor_id = tp.id1) as first_actor,
(select first_name || ' ' || last_name from actor where actor_id = tp.id2) as second_actor,
  f.title as title
from top_pair tp
    inner join film_actor fa1 on tp.id1 = fa1.actor_id
    inner join film_actor fa2 on tp.id2 = fa2.actor_id
    inner join film f on fa1.film_id=f.film_id and fa2.film_id=f.film_id