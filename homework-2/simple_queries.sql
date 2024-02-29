-- Запрос 1
SELECT contact_name, city
FROM customers;

-- Запрос 2
SELECT order_id, shipped_date - order_date AS days_to_ship
FROM orders;

-- Запрос 3
SELECT DISTINCT city
FROM customers;

-- Запрос 4
SELECT COUNT(*) AS order_count
FROM orders;

-- Запрос 5
SELECT COUNT(DISTINCT ship_country) AS country_count
FROM orders;
