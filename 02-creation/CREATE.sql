-- Дополнительное (необязательное) задание
-- В данном запросе создается таблица "Employee" с полями:
-- id - уникальный идентификатор сотрудника (автоинкрементируемый)
--  name - имя сотрудника
-- department - отдел, к которому относится сотрудник
-- manager_id - ссылка на начальника сотрудника
--- hire_date - дата принятия на работу сотрудника
-- salary - размер заработной платы сотрудника
-- email - электронная почта сотрудника
-- phone_number - номер телефона сотрудника

CREATE TABLE Employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    manager_id INT,
    hire_date DATE,
    salary DECIMAL(10, 2),
    email VARCHAR(50),
    phone_number VARCHAR(15),
    FOREIGN KEY (manager_id) REFERENCES Employee(id)
);

