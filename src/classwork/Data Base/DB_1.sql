-- DROP TABLE public.personal;

-- CREATE TABLE public.personal
-- (
-- <имя> <тип данных> <характеристики>
	-- id uuid        NOT NULL,
	-- name text      UNIQUE,
	-- age int        DEFAULT(18),
	-- height real    CHECK(100 < height AND height > 250),
	-- sex boolean,
	-- PRIMARY KEY(id, name)
-- )

SELECT * FROM public.personal;