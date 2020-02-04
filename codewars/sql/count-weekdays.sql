CREATE OR REPLACE FUNCTION weekdays(
   DATE, 
   DATE) 
RETURNS INTEGER 
LANGUAGE sql AS
$$
  SELECT COUNT(days)::int
  FROM generate_series(LEAST($1, $2), GREATEST($1, $2), '1 day') as days
  WHERE EXTRACT(DOW FROM days) NOT IN(0, 6);
$$;