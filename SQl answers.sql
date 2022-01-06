--a
SELECT count(Orders.OrderID)
From Orders, Shippers
Where Orders.ShipperID = Shippers.ShipperID
And Shippers.ShipperName = 'Speedy Express';

--count(Orders.OrderID)
--54

--b
SELECT LastName
FROM Employees,Orders
Where Employees.EmployeeID = Orders.EmployeeID
Group By Orders.EmployeeID
ORDER BY count(Orders.orderID)
LIMIT 1;

--LastName
--Dodsworth

--c
SELECT Products.ProductName
From Customers, OrderDetails, Orders, Products
Where Customers.CustomerID = Orders.CustomerId
And OrderDetails.OrderID = Orders.OrderID
AND Products.ProductID = OrderDetails.ProductID
AND Customers.Country = 'Germany'
Group By OrderDetails.ProductID
Order BY sum(OrderDetails.Quantity)
Limit 1;

--ProductName
--NuNuCa Nuß-Nougat-Creme