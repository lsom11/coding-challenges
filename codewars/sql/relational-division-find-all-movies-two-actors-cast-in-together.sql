SELECT f.title from film f
JOIN (
  select film_id from film_actor
  where actor_id in (105, 122)
  group by film_id
  having count(actor_id) = 2) fa
ON f.film_id =  fa.film_id
ORDER BY f.title

