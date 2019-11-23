SELECT DISTINCT CITY
FROM STATION
WHERE NOT SUBSTR(lower(CITY), 1, 1) IN ('a','e','i','o','u') OR
    NOT SUBSTR(lower(CITY), -1) IN ('a','e','i','o','u')