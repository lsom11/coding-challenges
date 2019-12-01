delete
FROM Person USING Person,
  Person p1
WHERE Person.id > p1.id
  AND Person.email = p1.email