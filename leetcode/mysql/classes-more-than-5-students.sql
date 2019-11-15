SELECT class from courses
GROUP BY class
HAVING COUNT(DISTINCT(student)) >= 5