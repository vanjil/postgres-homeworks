-- Запрос 1
SELECT c.company_name, CONCAT(e.first_name, ' ', e.last_name) AS employee_name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN employees e ON o.employee_id = e.employee_id
JOIN shippers s ON o.ship_via = s.shipper_id
WHERE c.city = 'London' AND e.city = 'London' AND s.company_name = 'United Package';

-- Запрос 2
SELECT p.product_name, p.units_in_stock, s.contact_name, s.phone
FROM products p
JOIN suppliers s ON p.supplier_id = s.supplier_id
WHERE p.discontinued <> 1
AND p.units_in_stock < 25
AND p.category_id IN (
    SELECT category_id
    FROM categories
    WHERE category_name IN ('Dairy Products', 'Condiments')
)
ORDER BY p.units_in_stock ASC;

-- Запрос 3
SELECT company_name
FROM customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id
    FROM orders
);

-- Запрос 4
SELECT DISTINCT product_name
FROM products
WHERE product_id IN (
    SELECT product_id
    FROM order_details
    WHERE quantity = 10
);



