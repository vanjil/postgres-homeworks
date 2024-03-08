-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student (
    student_id serial PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    birthday date,
    phone varchar
);

-- 2. Добавить в таблицу student колонку middle_name varchar

ALTER TABLE student
ADD COLUMN middle_name varchar;


-- 3. Удалить колонку middle_name
ALTER TABLE student
DROP COLUMN middle_name;


-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student
RENAME COLUMN birthday TO birthday_date;


-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student
ALTER COLUMN phone TYPE varchar(32);


-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name, last_name, birthday_date, phone)
VALUES ('Роза', 'Абрикосова', '01/02/1985', '917-250-3132');

INSERT INTO student (first_name, last_name, birthday_date, phone)
VALUES ('Тюльпан', 'Шестаков', '04/24/1985', '914-334-7778');

INSERT INTO student (first_name, last_name, birthday_date, phone)
VALUES ('Сирень', 'Кострюлькин', '02/12/1985', '914-766-9192');


-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
DELETE FROM student;
ALTER SEQUENCE student_student_id_seq RESTART WITH 1;