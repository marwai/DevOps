/*key = answer , notes, exercise, practice  **important 
*/
SELECT OrderID, CONVERT(VARCHAR(10),OrderDate,103) AS [dd/MM/yyyy]
FROM Orders; /* Before 2012 */

SELECT OrderID,FORMAT(OrderDate, 'dd/MM/yyyy')
FROM Orders; /*After2012*/
/*
Subquery 

the most commmon way to use it with the WHERE clause

The CONTAINING query(query)
*/

SELECT c.CompanyName AS "Customer"
FROM Customers c
WHERE c.CustomerID NOT IN 
    (SELECT o.CustomerID FROM Orders o);

SELECT * FROM Customers;
SELECT * FROM Orders;
    /*o.customerId not c.customerid because it is from orders*/

/*using joins do the same thing */
SELECT c.CompanyName AS "Customer"
FROM Customers c
FULL JOIN Orders o
on O.CustomerID = c.CustomerID
/*ANSWER JOIN exercise */
/* HAVING, GROUP BY, JOIN*/

SELECT c.CompanyName AS "Customer"
FROM orders o 
FULL JOIN customers c
ON c.customerID = o.CustomerID
GROUP BY O.CustomerID,c.CompanyName
HAVING o.CustomerID IS NULL

SELECT c.CompanyName AS "Customer"
FROM customers c
LEFT JOIN orders o
ON c.customerID = o.CustomerID
WHERE O.CustomerID IS NULL

--ANDREWS version
SELECT c.CompanyName AS "Customer"
FROM customers c 
FULL JOIN orders o ON c.customerID = o.CustomerID
WHERE o.CustomerID IS NULL

--practice 
SELECT c.CompanyName AS "Customer"
FROM orders o
right join customers c ON c.customerID = o.CustomerID
WHERE O.CustomerID IS NULL

/* notes
this is an example of an nested subquery in the SELECT clause (acts like a column)
Subqueries MUST be contained by brackets exlcuding alias
outputs the highest price in the table on every row in set
*/
SELECT OrderId, ProductID, UnitPrice, Quantity, Discount, 
    (SELECT MAX(UnitPrice) FROM[Order Details] od) AS "MAX Price"
FROM [Order details];

SELECT * FROM [Order Details];
--notes
/* This is an example of an inline view (select in from clause: acts like table) 
The inline view sq1 calculates the total for each product which is used to calculate percent of total
This is quite an advanced query 
In SSMS highlight part of the query and press F5 to execute/test part of your code

*/

SELECT od.ProductID, sq1.totalamt AS "Total sold for this Product",
UnitPrice, UnitPrice/totalamt*100*Quantity AS "% of Total"
    FROM [Order Details] od 
    INNER JOIN 
        (SELECT o.ProductID, SUM(o.UnitPrice*o.Quantity) AS totalamt
        FROM [Order Details] o
        GROUP BY o.ProductID) sq1 ON sq1.ProductID=od.ProductID

-- exercise 
/* Using a subquery in the WHERE clause, list all orders
from the [order details] table where the product has been discontinued

now repeat the same exercise using the simple join 
*/
--where
SELECT *
FROM 
[Order Details] od
WHERE od.ProductID IN (SELECT p.ProductID FROM Products p WHERE p.Discontinued =1);
--joins

SELECT *
FROM [Order Details]
right join Products c ON od.OrderID = p.OrderID
WHERE p.discontinued = 1 

/*baris version
*/
SELECT o.OrderID,p.ProductID,p.UnitPrice, od.Quantity, od.Discount
FROM Orders o
INNER JOIN [Order Details] od
ON o.OrderID=od.OrderID
INNER JOIN Products p
ON od.ProductID=p.ProductID
WHERE p.ProductID IN (SELECT p.ProductID FROM Products p WHERE p.Discontinued =1)

--Answer **
SELECT od.OrderID,od.ProductID,p.UnitPrice, od.Quantity, od.Discount
FROM [Order Details] od
INNER JOIN products p
ON od.ProductID = p.ProductID
WHERE p.discontinued =1

--NOTES
/* This is  a contrived example showing how you could list all employee IDs in the same column as all SupplierIDs 
UNION ALL returns 38 rows
UNION removes any duplicates and returns 29 rows
Both SELECT statements must have the same number of columns in the SELECT claue (same type)
    only the Column Alias in the first SELECT will be applied
ORDER BY 1 may be more appropriate if  

Similiar to Inner Join without the relationship neither has the same fuctionality. 
*/
SELECT * FROM Employees
SELECT * FROM SUPPLIERS

SELECT e.EmployeeID AS "Employee/Supplier"
FROM Employees e
UNION 
SELECT s.supplierID
FROM Suppliers s

SELECT e.EmployeeID AS "Employee/Supplier"
FROM Employees e
UNION ALL
SELECT s.supplierID
FROM Suppliers s

select * from Orders