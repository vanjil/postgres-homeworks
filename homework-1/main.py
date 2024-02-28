import os
import psycopg2
import csv

# Функция для получения данных из CSV файла
def get_data_from_csv(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

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
    # Создание таблицы customers_data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers_data (
            customer_id VARCHAR(10) PRIMARY KEY,
            company_name VARCHAR(50) NOT NULL,
            contact_name VARCHAR(30) NOT NULL
        );
    """)

    # Создание таблицы employees_data
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

    # Создание таблицы orders_data
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

# Заполнение таблиц данными из CSV файлов
try:
    # Папка, в которой содержатся файлы CSV
    base_path = 'north_data'

    # Перебор всех файлов CSV в каждой папке
    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if os.path.isdir(folder_path):
            for csv_file in os.listdir(folder_path):
                if csv_file.endswith('.csv'):
                    file_path = os.path.join(folder_path, csv_file)
                    data = get_data_from_csv(file_path)

                    # Вставка данных в соответствующую таблицу
                    if folder == 'customers_data':
                        for row in data:
                            cursor.execute(
                                """
                                INSERT INTO customers_data (customer_id, company_name, contact_name)
                                VALUES (%s, %s, %s)
                                """,
                                (row['customer_id'], row['company_name'], row['contact_name'])
                            )
                    elif folder == 'employees_data':
                        for row in data:
                            cursor.execute(
                                """
                                INSERT INTO employees_data (employee_id, first_name, last_name, title, birth_date, notes)
                                VALUES (%s, %s, %s, %s, %s, %s)
                                """,
                                (row['employee_id'], row['first_name'], row['last_name'], row['title'],
                                 row['birth_date'], row['notes'])
                            )
                    elif folder == 'orders_data':
                        for row in data:
                            cursor.execute(
                                """
                                INSERT INTO orders_data (order_id, customer_id, employee_id, order_date, ship_city)
                                VALUES (%s, %s, %s, %s, %s)
                                """,
                                (row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city'])
                            )

    connection.commit()
    print("Данные успешно добавлены в таблицы!")
except Exception as e:
    print(f"Ошибка добавления данных: {e}")
    connection.rollback()

# Закрытие соединения
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
