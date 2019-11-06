SELECT e.name AS employee 
    FROM Employee e LEFT JOIN Employee m ON e.ManagerId = m.Id
    WHERE e.Salary > m.Salary
