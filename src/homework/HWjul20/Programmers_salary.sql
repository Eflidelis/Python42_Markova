DROP TABLE IF EXISTS castomers CASCADE;
DROP TABLE IF EXISTS projects CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP TABLE IF EXISTS programmers CASCADE;
DROP TABLE IF EXISTS project_managers CASCADE;
DROP TABLE IF EXISTS team CASCADE;

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE castomers (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    name VARCHAR(50),
    contact VARCHAR(50),
    telephone TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE projects (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    castomer_id uuid REFERENCES castomers(id) ON DELETE CASCADE,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    title TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE programmers (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL,
    birthday TEXT,
    level VARCHAR(20),
    telephone TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE tasks (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    project_id uuid REFERENCES projects(id) ON DELETE CASCADE,
    description TEXT,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE project_managers (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    name VARCHAR(50),
    birthday TEXT,
    telephone TEXT,
    project_id uuid REFERENCES projects(id) ON DELETE CASCADE,
    PRIMARY KEY(id)
);

CREATE TABLE team (
    task_id uuid REFERENCES tasks(id) ON DELETE CASCADE,
    programmer_id uuid REFERENCES programmers(id) ON DELETE CASCADE,
    PRIMARY KEY (task_id, programmer_id)
);

INSERT INTO castomers(name, contact, telephone) VALUES
('Яргорэлектротранс', 'Мария Ивановна', '12-34-56'),
('Газпром', 'Павел Петрович', '23-45-67'),
('Пятерочка', 'Снежанна Денисовна', '34-56-78');

INSERT INTO projects(castomer_id, start_date, end_date, title) VALUES
((SELECT id FROM castomers WHERE name = 'Яргорэлектротранс'), '2025-07-01', '2025-10-12', 'обновление системы оплаты проезда'),
((SELECT id FROM castomers WHERE name = 'Газпром'), '2025-05-20', '2025-07-12', 'разработка мобильного приложения'),
((SELECT id FROM castomers WHERE name = 'Пятерочка'), '2025-06-30', '2025-09-01', 'дизайн сайта со скидками');

INSERT INTO programmers(name, birthday, level, telephone) VALUES
('Вася', '1990-01-03', 'джун', '10-10-10'),
('Петя', '1980-08-13', 'мидл', '11-11-11'),
('Юра', '1995-05-10', 'сеньор', '12-12-12'),
('Маша', '1998-07-16', 'джун', '13-13-13'),
('Витя', '2000-04-30', 'мидл', '14-14-14'),
('Зоя', '1997-06-05', 'сеньор', '15-15-15');

INSERT INTO tasks(project_id, description, start_date, end_date) VALUES
((SELECT id FROM projects WHERE title = 'обновление системы оплаты проезда'), 'задача 1', '2025-07-01', '2025-07-03'),
((SELECT id FROM projects WHERE title = 'обновление системы оплаты проезда'), 'задача 2', '2025-07-04', '2025-07-11'),
((SELECT id FROM projects WHERE title = 'разработка мобильного приложения'), 'задача 3', '2025-05-20', '2025-07-05'),
((SELECT id FROM projects WHERE title = 'разработка мобильного приложения'), 'задача 4', '2025-07-06', '2025-07-11'),
((SELECT id FROM projects WHERE title = 'дизайн сайта со скидками'), 'задача 5', '2025-06-30', '2025-08-15'),
((SELECT id FROM projects WHERE title = 'дизайн сайта со скидками'), 'задача 6', '2025-08-16', '2025-08-28');

INSERT INTO project_managers(name, birthday, telephone, project_id) VALUES
('Порфирий', '1970-02-15', '22-33-44', (SELECT id FROM projects WHERE title = 'обновление системы оплаты проезда')),
('Иннокентий', '1980-06-25', '33-44-55', (SELECT id FROM projects WHERE title = 'разработка мобильного приложения')),
('Евфстрахий', '1997-07-07', '44-55-66', (SELECT id FROM projects WHERE title = 'дизайн сайта со скидками'));

INSERT INTO team(task_id, programmer_id) VALUES
((SELECT id FROM tasks WHERE description = 'задача 1'), (SELECT id FROM programmers WHERE name = 'Вася')),
((SELECT id FROM tasks WHERE description = 'задача 1'), (SELECT id FROM programmers WHERE name = 'Петя')),
((SELECT id FROM tasks WHERE description = 'задача 2'), (SELECT id FROM programmers WHERE name = 'Юра')),
((SELECT id FROM tasks WHERE description = 'задача 3'), (SELECT id FROM programmers WHERE name = 'Маша')),
((SELECT id FROM tasks WHERE description = 'задача 5'), (SELECT id FROM programmers WHERE name = 'Витя')),
((SELECT id FROM tasks WHERE description = 'задача 6'), (SELECT id FROM programmers WHERE name = 'Зоя'));

-- запрос
SELECT 
    castomers.name AS заказчик,
    projects.title AS проект,
    project_managers.name AS проект_менеджер,
    tasks.description AS задача,
    programmers.name AS ответственный_за_задачу,
    programmers.telephone AS телефон_программиста
FROM 
    castomers 
JOIN 
    projects ON castomers.id = projects.castomer_id 
JOIN 
    project_managers ON projects.id = project_managers.project_id 
JOIN 
    tasks ON projects.id = tasks.project_id 
JOIN 
    team ON tasks.id = team.task_id 
JOIN 
    programmers ON team.programmer_id = programmers.id;

ALTER TABLE castomers ADD COLUMN price DECIMAL(10, 2);
ALTER TABLE programmers ADD COLUMN salary DECIMAL(10, 2);
ALTER TABLE project_managers ADD COLUMN salary DECIMAL(10, 2);


UPDATE castomers SET price = 10000 WHERE name = 'Яргорэлектротранс';
UPDATE castomers SET price = 15000 WHERE name = 'Газпром';
UPDATE castomers SET price = 8000 WHERE name = 'Пятерочка';

UPDATE programmers SET salary = 5000 WHERE name = 'Вася';
UPDATE programmers SET salary = 6000 WHERE name = 'Петя';
UPDATE programmers SET salary = 7000 WHERE name = 'Юра';
UPDATE programmers SET salary = 4000 WHERE name = 'Маша';
UPDATE programmers SET salary = 5500 WHERE name = 'Витя';
UPDATE programmers SET salary = 6500 WHERE name = 'Зоя';

UPDATE project_managers SET salary = 8000 WHERE name = 'Порфирий';
UPDATE project_managers SET salary = 9000 WHERE name = 'Иннокентий';
UPDATE project_managers SET salary = 7000 WHERE name = 'Евфстрахий';


SELECT 
    castomers.name AS заказчик,
    castomers.price AS сколько_он_заплатил,
    projects.title AS проект,
    tasks.description AS задача,
    (SELECT SUM(salary) FROM programmers WHERE id IN (SELECT programmer_id FROM team WHERE task_id = tasks.id)) AS сколько_денег_ушло_на_данную_задачу
FROM 
    castomers 
JOIN 
    projects ON castomers.id = projects.castomer_id 
JOIN 
    tasks ON projects.id = tasks.project_id;
