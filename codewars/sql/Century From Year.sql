SELECT 
  CASE
    WHEN yr::varchar LIKE '%00' THEN CEILING(yr / 100)
    ELSE CEILING(yr / 100) + 1
  END AS century
FROM years