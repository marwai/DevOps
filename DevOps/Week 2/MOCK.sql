
/*1. Create a report showing the title of courtesy and the first and last name
of all employees whose title of courtesy is not "Ms." or "Mrs.".*/
--select * from Employees

SELECT e.FirstName, e.LastName 
FROM Employees e 
WHERE e.TitleOfCourtesy NOT IN ('Ms.', 'Mrs.')


/*2. Create a report that shows the company name, contact title, city and country of all customers 
in Mexico or in any city in Spain except Madrid(in Spain).*/

SELECT c.CompanyName, c.ContactTitle, c.City, c.Country 
from customers c  
    WHERE (c.Country = 'mexico'
    OR  c.Country = 'spain') AND C.city != 'madrid'
--brackets
/*3. Create a report showing the title of courtesy and the first and
last name of all employees whose title of courtesy begins with "M" and
is followed by any character and a period (.).*/

SELECT e.TitleOfCourtesy, e.FirstName, e.LastName 
FROM Employees e
where e.TitleOfCourtesy LIKE 'm%' 

--correction 
/* character(s)
where e.TitleOfCourtesy LIKE 'm_%.' 
*/

/*4. Create a report showing the first and last names of
all employees whose region is defined.*/

SELECT e.FirstName, e.LastName 
FROM Employees e 
WHERE Region IS NOT NULL



/*5. Select the Title, FirstName and LastName columns from the Employees table.
  Sort first by Title in ascending order and then by LastName 
   in descending order.*/


SELECT e.Title, e.FirstName, e.LastName 
FROM Employees e
ORDER BY e.Title,LastName DESC ;
-- default asc

/*6. Write a query to get the number of employees with the same job title.*/
select * from Employees

SELECT E.TITLE, COUNT(*) AS "the number of employees with the same job title" FROM Employees e
GROUP BY e.Title 

/*7.
Create a report showing the Order ID, the name of the company that placed the order,
and the first and last name of the associated employee.
Only show orders placed after January 1, 1998 that shipped after they were required.
Sort by Company Name.
*/




/*8.Create a report that shows the total quantity of products (from the OrderDetails table) ordered.
Only show records for products 
for which the quantity ordered is fewer than 200. 
The report should return*/





/*9.Create a report that shows the total number of orders by Customer since December 31, 1996. The report 
should only return rows for which the NumOrders is greater than 15. 
*/
/*can use where clause because it is in orders
group by because states "each customer or per customer"*
HAVING using aggregate functions (SUM,avg etc) and group by
*/
SELECT c.CustomerID, COUNT(o.OrderID) AS "NumOrders"
FROM Customers c JOIN Orders o ON
    (c.CustomerID = o.CustomerID)
WHERE OrderDate >= '31-Dec-1996'
GROUP BY c.CustomerID
HAVING COUNT(o.OrderID) > 15


/*10.  SQL statement will return all customers, and number of orders they might have placed. 
Include those customers as well who have not placed any orders.*/

SELECT c.CustomerID, COUNT(o.OrderID) AS "Number Of Orders Placed by Customer"
FROM Orders o RIGHT JOIN customers c 
ON c.CustomerID=o.CustomerID
GROUP BY c.CustomerID

-- left join, right join or inner in exam

/*
reference between foreign key and primary integrity 
primary key foreign relationship 1:n is 1 too many