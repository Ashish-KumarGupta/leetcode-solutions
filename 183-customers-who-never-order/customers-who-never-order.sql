# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers
LEFT JOIN orders
On Customers.id = Orders.customerId
WHERE orders.customerId IS Null;