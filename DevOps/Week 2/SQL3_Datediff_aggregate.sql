SELECT DATEADD(d,5,OrderDate) AS "Due Date",
    DATEDIFF(d,OrderDate,ShippedDate) AS "Ship Days"
    FROM Orders;
/* notes */


/* Getting Age */
SELECT CONCAT(e.Firstname,' ', e.LastName) AS "Employee Name", DATEDIFF( YEAR,BirthDate,GETDATE()) AS "Age"
FROM Employees e;

DECLARE @test DECIMAL(18,6) = 123.456789 AS "Number of decimal places"
SELECT FORMAT(@test, '##.##')

SELECT CONCAT(e.Firstname,' ', e.LastName) AS "Employee Name", FORMAT(DATEDIFF( day,BirthDate,GETDATE()) / 365.25, '##.##') AS "Age"
FROM Employees e;

SELECT CONCAT(e.Firstname,' ', e.LastName) AS "Employee Name", DATEDIFF( day,BirthDate,GETDATE()) / 365.25 AS "Age"
FROM Employees e;


SELECT CONCAT(e.Firstname,' ', e.LastName) 
AS "Employee Name",DATEDIFF( HOUR,BirthDate,GETDATE()) / 8766.00000
AS "Age"
FROM Employees e;

SELECT CASE 
WHEN DATEDIFF(d,OrderDate,ShippedDate) < 10 THEN 'On Time'
ELSE 'Overdue'
END AS "Status"
FROM orders

SELECT * FROM orders

SELECT CASE 
WHEN DATEDIFF(YEAR,BirthDate,GETDATE()) > 65 THEN 'Retired'
WHEN DATEDIFF(YEAR,BirthDate,GETDATE()) > 60 THEN 'Retirement due'
ELSE  'More than 5 years to go'
END AS "Retirement Status"
FROM Employees

SELECT CONCAT(FirstName, ' ', LastName) AS "Name"
        , DATEDIFF(YY,BirthDate,GETDATE()) AS "Age",
CASE 
WHEN DATEDIFF(YY,e.BirthDate,GETDATE()) >= 65 THEN 'Retired'
WHEN DATEDIFF(YY,e.BirthDate,GETDATE()) >= 60 THEN 'Retirement due'
ELSE  'More than 5 years to go'
END AS "Retirement Status"
FROM Employees e ;


SELECT SUM(p.UnitsOnOrder) AS "Total On Order",
    AVG(p.UnitsOnOrder) AS "Avg on Order",
    MIN(p.UnitsOnOrder) AS "Min on Order",
    MAX(p.UnitsOnOrder) AS "Max on Order"
    FROM Products P
  
  SELECT SupplierID, SUM(p.UnitsOnOrder) AS "Total On Order",
    AVG(p.UnitsInStock) AS "Avg on Order",
    MIN(p.UnitsOnOrder) AS "Min on Order",
    MAX(p.UnitsOnOrder) AS "Max on Order"
    FROM Products P
    GROUP BY SupplierID

SELECT * FROM Products  
/*Calculate Units on Order using aggregate function per supplier*/

--Max,23,25,26 : Marcus 29,28,30
SELECT * FROM Products
SELECT CategoryID, SUM(p.ProductsOnOrder) AS "Total"


/* 
Use GROUP BY to calculate the average Reorder Level for all Proudcts by CategoryID
Remember the SELECT clause must match the GROUP BY clause apart from any aggregates
What is the highest Average Reorer Level? Use ORDER BY with DESC to confirm
NOTE: you can use column alias in the ORDER BY clause (due to processing sequece)
*/
 SELECT  CategoryID,
 AVG(p.ReorderLevel) AS "Average Reorder Level"
    FROM Products P
    GROUP BY p.CategoryID
    ORDER BY "Average Reorder Level" DESC

/* HAVING clause 
HAVING is used instead of WHERE when filtering on subtotals/grouped data
Column Aliases cannot be used in the HAVING CLAUSE 
*/
/*aggregate examples - COUNT */
-- Example 1
SELECT SupplierID,
SUM(UnitsOnOrder) AS "Total on Order",
    AVG(UnitsOnOrder) AS "Avg on Order"
    FROM Products  
    GROUP BY SupplierID
    HAVING AVG(UnitsonOrder)>5

--Example 2 
  SELECT SupplierID, SUM(p.UnitsOnOrder) AS "Total On Order",
    AVG(p.UnitsInStock) AS "Avg on Order",
    MIN(p.UnitsOnOrder) AS "Min on Order",
    MAX(p.UnitsOnOrder) AS "Max on Order"
    FROM Products P
    GROUP BY SupplierID
    HAVING AVG(p.UnitsOnOrder) >5
/* ALL DONE */
Edgar F.Codd

/*


/* HAVING AND WHERE*/

/* JOINS ASTHA*/
-- 7.13 -- 

CREATE TABLE student
VALUES
(
        'Nicole'
)

SELECT * FROM student
SELECT * FROM [Customer and Suppliers by City

/* exercise*/
SELECT * FROM course c INNER JOIN student s ON s.course_id=c.c_id

SELECT 
FROM Orders o INNER JOIN Employee
/* eXERCISE*/ 
SELECT * FROM Products
SELECT p.Product Name, p.SupplierId
GROUP BY SupplierID

  SELECT  s.CompanyName as "Supplier Name",
    AVG(p.UnitsOnOrder) 
  AS "Average units on order"
  FROM products p
  INNER JOIN Suppliers s
  ON p.SupplierID=s.SupplierID
  GROUP BY s.SupplierID, s.CompanyName
  ORDER BY "Average units on order" DESC 


SELECT * FROM Products
SELECT * FROM Suppliers

SELECT s.CompanyName as "Supplier Name", AVG(p.UnitsOnOrder) 
AS "Average units on order"
FROM Products p 
INNER JOIN Suppliers s 
ON p.SupplierID = s.SupplierID
GROUP BY s.SupplierID, s.CompanyName

CREATE TABLE student
(
    st_id INT IDENTITY(1,1),
    student_name VARCHAR(30),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES course(c_id) ON DELETE CASCADE

)

DROP TABLE course
CREATE TABLE course  
(
    c_id INT IDENTITY(1,1) PRIMARY KEY,
    course_name VARCHAR(30)
)

INSERT INTO course
(
    course_name
)
VALUES
(
    'Business' 
),
(
    'Test'
),
(
    'Agile'
),
(
    'Web'
),
(
    'Dev'
)


INSERT INTO student
(
   student_name, course_id 
)
VALUES
(
    'Lee', 1
),
(
    'Barry', 1
),
(
    'David', 2
),
(
    'Tim',5
),
(
    'Nicole',3
)


INSERT INTO student
(
   student_name
)
VALUES
(
    'Nicole'   
)

SELECT * FROM student
SELECT * FROM course

SELECT * FROM course c INNER JOIN student s
ON s.course_id=c.c_id

SELECT * FROM customers
select * from orders

select o.orderId, o.orderDate, o.freight, 
c.CompanyName AS "Customer Name", 
CONCAT(FirstName,' ', LastName) AS "Employee Name" from employees e
inner join  orders o   ON o.EmployeeID = e. EmployeeID
inner join customers c ON c.CustomerID = o.CustomerID
ORDER BY o.orderID DESC;