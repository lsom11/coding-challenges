SELECT 
    CASE
        WHEN a + b <= c or a + c <= b or b + c <= a THEN 'Not A Triangle'
        WHEN a = b AND b = c THEN 'Equilateral'
        WHEN a = b OR a = c OR b = c THEN 'Isosceles'
        ELSE 'Scalene'
    END AS triangles_type
FROM TRIANGLES