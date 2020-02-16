SELECT 
  th.id as id,
  heads,
  arms,
  legs,
  tails,
  CASE
    WHEN (th.heads > th.arms) OR (bh.tails > bh.legs) THEN 'BEAST'
    ELSE 'WEIRDO'
  END as species
FROM top_half th
LEFT JOIN bottom_half bh ON th.id = bh.id
ORDER BY species