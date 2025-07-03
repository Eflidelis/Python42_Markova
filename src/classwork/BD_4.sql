DROP TABLE IF EXISTS castomers CASCADE;
DROP TABLE IF EXISTS projects CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP TABLE IF EXISTS programmers CASCADE;
DROP TABLE IF EXISTS project_managers CASCADE;

create extension if not exists "pgcripto";

CREATE TABLE castomers(
id uuid NOT NULL DEFAULT gen_random_uuid(),
name VARCHAR(50),
contact VARCHAR(50),
telephone TEXT
PRIMARY KEY(id)
);


CREATE TABLE projects(
id uuid NOT NULL DEFAULT gen_random_uuid(),
castomer_id uuid REFERENCES castomers(id) ON DELETE CASCADE,
start TEXT NOT NULL,
end TEXT NOT NULL,
title TEXT,
PRIMARY KEY(id)
);


CREATE TABLE programmers(
id uuid NOT NULL DEFAULT gen_random_uuid(),
name VARCHAR(50) NOT NULL,
birthday TEXT,
level VARCHAR(20),
telephone TEXT,
PRIMARY KEY(id)
);


CREATE TABLE tasks(
id uuid NOT NULL DEFAULT gen_random_uuid(),
project_id uuid REFERENCES projects(id) ON DELETE CASCADE,
description TEXT,
start TEXT NOT NULL,
end TEXT NOT NULL,
programmer_id uuid REFERENCES programmers(id) ON DELETE CASCADE,
PRIMARY KEY(id)
);


CREATE TABLE project_managers(
id uuid NOT NULL DEFAULT gen_random_uuid(),
name VARCHAR(50),
birthday TEXT,
telephone TEXT,
project_id uuid REFERENCES projects(id) ON DELETE CASCADE,
PRIMARY KEY(id)
);


INSERT INTO castomers(name, contact, telephone) VALUES
('Яргорэлектротранс', 'Мария Ивановна', '12-34-56'),
('Газпром', 'Павел Петрович', '23-45-67'),
('Пятерочка', 'Снежанна Денисовна', '34-56-78');

INSERT INTO projects(castomer_id, start, end, title) VALUES
((SELECT id FROM castomers WHERE name = 'Яргорэлектротранс'), '1 июля 2025', '12 октября 2015', 'обновление системы оплаты проезда'),
((SELECT id FROM castomers WHERE name = 'Газпром'), '20 мая 2025', '12 июля 2025', 'разработка мобильного приложения'),
((SELECT id FROM castomers WHERE name = 'Пятерочка'), '30 июня 2025', '1 сентября 2025', 'дизайн сайта со скидками');

INSERT INTO programmers(name, birthday, level, telephone) VALUES
('Вася', '1/3/1990', '5 lvl', '10-10-10'),
('Петя', '13/8/1980', '7 lvl', '11-11-11'),
('Юра', '10/5/1995', '10 lvl', '12-12-12'),
('Маша', '16/7/1998', '3 lvl', '13-13-13'),
('Витя', '30/4/2000', '8 lvl', '14-14-14'),
('Зоя', '5/6/1997', '11 lvl', '15-15-15');

INSERT INTO tasks(project_id, description, start, end, programmer_id) VALUES
((SELECT id FROM projects WHERE title = 'обновление системы оплаты проезда'), 'задача 1', '1.07', '3.07', (SELECT id FROM programmers WHERE name = 'Вася')),
((SELECT id FROM projects WHERE title = 'обновление системы оплаты проезда'), 'задача 2', '4.07', '11.07', (SELECT id FROM programmers WHERE name = 'Петя')),
((SELECT id FROM projects WHERE title = 'разработка мобильного приложения'), 'задача 3', '20.05', '5.07', (SELECT id FROM programmers WHERE name = 'Юра')),
((SELECT id FROM projects WHERE title = 'разработка мобильного приложения'), 'задача 4', '6.07', '11.07', (SELECT id FROM programmers WHERE name = 'Маша')),
((SELECT id FROM projects WHERE title = 'дизайн сайта со скидками'), 'задача 5', '30.06', '15.08', (SELECT id FROM programmers WHERE name = 'Витя')),
((SELECT id FROM projects WHERE title = 'дизайн сайта со скидками'), 'задача 6', '16.08', '28.08', (SELECT id FROM programmers WHERE name = 'Зоя'));


INSERT INTO project_managers(name, birthday, telephone, project_id) VALUES
('Порфирий', '15/2/1970', '22-33-44', (SELECT id FROM projects WHERE title = 'обновление системы оплаты проезда')),
('Иннокентий', '25/6/1980', '33-44-55', (SELECT id FROM projects WHERE title = 'разработка мобильного приложения')),
('Евфстрахий', '7/7/1997', '44-55-66', (SELECT id FROM projects WHERE title = 'дизайн сайта со скидками'));

SELECT castomers.name AS castomer, projects.title AS project, project_managers.name AS manager, 
programmers.name AS programmer, programmers.telephone AS telephone
FROM castomers JOIN projects ON castomers.id = projects.castomer_id 
JOIN manager ON projects.id = project_managers.project_id
JOIN tasks ON tasks.id = tasks.project_id











