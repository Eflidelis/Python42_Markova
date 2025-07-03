-- DROP TABLE groups;

-- CREATE TABLE groups
-- (
-- 	id uuid NOT NULL,
-- 	name text,
-- 	form_ed text,

-- 	PRIMARY KEY(id)
-- );

-- DROP TABLE students;

-- CREATE TABLE students
--  (
-- 	 id uuid NOT NULL,
-- 	 name text,
-- 	 age int,
-- 	 grade float,
-- 	 gr uuid,

-- 	 PRIMARY KEY(id),
-- 	 FOREIGN KEY(gr)
-- 	 REFERENCES groups (id)
-- 	 ON DELETE SET NULL
-- 	 ON UPDATE CASCADE
--  );

-- INSERT INTO groups VALUES
-- 	('25a5a783-5176-49c9-ae51-455817c9146e', 'Ro55', 'заочная'),
-- 	('54e5fc81-a6e9-4cf9-ab93-ae14cee6969e', 'Ja13', 'заочная'),
-- 	('d532d81b-77c9-4d05-9597-f6d10ef75c19', 'Tu74', 'очная');
	
-- 	('0d609da6-ed2c-4ad9-b460-64de194ac898','Py42', 'очная');

-- INSERT INTO students VALUES
-- -- 	('5f8012df-cd1c-4c7f-9a76-e38ea7156e56', 'Наталья', '39', '4.2', '0d609da6-ed2c-4ad9-b460-64de194ac898' ),
-- -- 	('4a8ddc8a-9e52-4326-aa3d-373fdb6459e6', 'Ирина', '30', '4.3', '25a5a783-5176-49c9-ae51-455817c9146e' ),
-- -- 	('b4c2aefb-3882-4a09-8251-9218d847c6eb', 'Виталий', '45', '3.5', '25a5a783-5176-49c9-ae51-455817c9146e' ),
-- -- 	('5cf2f8f3-d2f9-44cd-8ef0-b29ce95894c5', 'Денис', '25', '4.0', 'd532d81b-77c9-4d05-9597-f6d10ef75c19' ),
-- -- 	('0c60da8c-3670-4cc2-933d-dc86da480070', 'Владимир', '32', '3.8', 'd532d81b-77c9-4d05-9597-f6d10ef75c19' );
-- 	('fc47d17a-6c6a-419a-ba8d-c63f14e929b4', 'Марина', '30', '4.7', '25a5a783-5176-49c9-ae51-455817c9146e' ),
--  	('81c84af4-945a-4b57-b660-b0fd17c6fd8f', 'Георгий', '45', '3.0', '25a5a783-5176-49c9-ae51-455817c9146e' ),
--  	('0c54cff6-a4b3-4344-bf6c-1e71dd92ee46', 'Даниил', '25', '4.8', 'd532d81b-77c9-4d05-9597-f6d10ef75c19' ),
--  	('21e3772c-411f-428e-a2e0-c7f5d19cf750', 'Елисей', '32', '3.6', 'd532d81b-77c9-4d05-9597-f6d10ef75c19' );

-- SELECT * FROM students;
-- SELECT * FROM groups;

-- select name, age, grade from students where age > 30 AND grade < 4;

-- SELECT students.name, age, grade, groups.name as group from students, groups
	-- where students.gr = groups.id AND groups.name = 'Py42';

-- SELECT students.name as student, age, grade, groups.name as group
-- 	from groups, students
-- 	where groups.id = students.gr AND groups.name = 'Py42';

-- delete from groups where id = 'd532d81b-77c9-4d05-9597-f6d10ef75c19';

SELECT students.name as student, age, grade, groups.name as group
	from groups, students
	where groups.id = students.gr AND groups.name = 'Py42';



