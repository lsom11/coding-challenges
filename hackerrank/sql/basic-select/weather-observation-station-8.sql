SELECT DISTINCT CITY
FROM STATION
WHERE  SUBSTR(lower(CITY),1,1) IN ('a','e','i','o','u') AND SUBSTR(lower(CITY),-1) IN ('a','e','i','o','u');