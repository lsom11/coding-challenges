SELECT
  MIN(score),
  ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY score)::numeric, 2)::float as median,
  MAX(score)
FROM result;