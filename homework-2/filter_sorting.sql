-- Запрос 1
SELECT *
FROM orders
WHERE ship_country IN ('France', 'Germany', 'Spain');

-- Запрос 2
SELECT DISTINCT ship_country, ship_city
FROM orders
ORDER BY ship_country, ship_city;

-- Запрос 3
SELECT AVG(shipped_date - order_date) AS average_delivery_time
FROM orders
WHERE ship_country = 'Germany';

-- Запрос 4
SELECT MIN(unit_price) AS min_price, MAX(unit_price) AS max_price
FROM products
WHERE discontinued <> 1;

-- Запрос 5
SELECT MIN(unit_price) AS min_price, MAX(unit_price) AS max_price
FROM products
WHERE discontinued <> 1 AND units_in_stock >= 20;
