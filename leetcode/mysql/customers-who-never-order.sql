SELECT Name AS Customers FROM Customers c LEFT JOIN Orders o ON c.id = o.CustomerId WHERE CustomerId IS NULL


