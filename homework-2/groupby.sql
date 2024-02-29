-- Запрос 1
SELECT DISTINCT ship_city, ship_country
FROM orders
WHERE ship_city LIKE '%burg';

-- Запрос 2
SELECT order_id, customer_id, freight, ship_country
FROM orders
WHERE ship_country LIKE 'P%'
ORDER BY freight DESC
LIMIT 10;

-- Запрос 3
SELECT first_name, last_name, phone
FROM employees
WHERE region IS NULL;

-- Запрос 4
SELECT country, COUNT(*) AS supplier_count
FROM suppliers
GROUP BY country
ORDER BY supplier_count DESC;

-- Запрос 5
SELECT ship_country, SUM(freight) AS total_weight
FROM orders
WHERE ship_region IS NOT NULL
GROUP BY ship_country
HAVING SUM(freight) > 2750
ORDER BY total_weight DESC;

-- Запрос 6
SELECT country
FROM customers
INTERSECT
SELECT country
FROM suppliers
INTERSECT
SELECT country
FROM employees;

-- Запрос 7
SELECT country
FROM customers
INTERSECT
SELECT country
FROM suppliers
EXCEPT
SELECT country
FROM employees;
