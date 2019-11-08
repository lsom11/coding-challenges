SELECT id, movie, description, rating FROM cinema WHERE MOD(id, 2) != 0 AND description != 'boring'
ORDER BY rating DESC