import psycopg2

# Подключение к базе данных
try:
    connection = psycopg2.connect(
        database="north",
        user="postgres",
        password="мдфвшьшк",
        host="localhost",
        port="5432",
    )
    cursor = connection.cursor()
except Exception as e:
    print(f"Ошибка подключения: {e}")
    exit()

# Создание таблиц
try:
    # Customers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers_data (
            customer_id VARCHAR(10) PRIMARY KEY,
            company_name VARCHAR(50) NOT NULL,
            contact_name VARCHAR(30) NOT NULL
        );
    """)

    # Employees
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees_data (
            employee_id VARCHAR(10) PRIMARY KEY,
            first_name VARCHAR(15) NOT NULL,
            last_name VARCHAR(15) NOT NULL,
            title VARCHAR(30) NOT NULL,
            birth_date DATE NOT NULL,
            notes VARCHAR(1000) NOT NULL
        );
    """)

    # Orders
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders_data (
            order_id VARCHAR(5) PRIMARY KEY,
            customer_id VARCHAR(10) REFERENCES customers_data(customer_id),
            employee_id VARCHAR(10) REFERENCES employees_data(employee_id),
            order_date DATE NOT NULL,
            ship_city VARCHAR(20) NOT NULL
        );
    """)

    connection.commit()
    print("Таблицы созданы успешно!")
except Exception as e:
    print(f"Ошибка создания таблиц: {e}")
    connection.rollback()

# Закрытие соединения
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
