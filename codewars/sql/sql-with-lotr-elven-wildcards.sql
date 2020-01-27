SELECT CONCAT(INITCAP(firstname), ' ', INITCAP(lastname)) as shortlist FROM Elves e
WHERE e.firstname LIKE '%tegil%' OR e.lastname LIKE '%astar%'
