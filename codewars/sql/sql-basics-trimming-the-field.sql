SELECT
  id,
  name,
  substring(characteristics FROM '([a-z]+)') AS characteristic
FROM monsters
ORDER BY id ASC;