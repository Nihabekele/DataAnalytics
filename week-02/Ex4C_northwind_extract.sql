-- 4a) The items Northwind sells are stored in the products table.
-- 4b) The categories or types of items are stored in the categories table.

-- 5) Retrieve all columns from the employees table
SELECT * FROM northwind.employees;

-- 5a) The employee whose name looks like a bird is Margaret Peacock.

-- 6) Retrieve all columns from the products table
SELECT * FROM northwind.products;

-- 6a) The query returns 77 records. products
-- To change it to 10 rows using the toolbar, I use the "Limit to" dropdown menu.

-- 6b) BONUS: To limit the rows in the code, I use the LIMIT clause.
SELECT * FROM northwind.products LIMIT 10;
-- Source: MySQL Documentation

SELECT * FROM northwind.categories;
-- 7c) The category ID for Seafood is 8.
SELECT OrderID, OrderDate, ShipName, ShipCountry 
FROM northwind.orders 
LIMIT 50;


























