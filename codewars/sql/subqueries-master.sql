SELECT 
  CASE
  WHEN LENGTH(name) - LENGTH(REPLACE(name, ' ', '')) > 2 THEN
    CONCAT(split_part(name, ' ', 1), ' ', split_part(name, ' ', 2))
  ELSE
    split_part(name, ' ', 1)
  END as name,
  
  CASE
  WHEN LENGTH(name) - LENGTH(REPLACE(name, ' ', '')) > 2 THEN
    split_part(name, ' ', 3)
  ELSE
    split_part(name, ' ', 2)
  END as first_lastname,
  
  CASE
  WHEN LENGTH(name) - LENGTH(REPLACE(name, ' ', '')) > 2 THEN
    split_part(name, ' ', 4)
  ELSE
    split_part(name, ' ', 3)
  END as second_lastname
FROM people
