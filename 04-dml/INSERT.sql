-- Домашнее задание к лекции «Продвинутая выборка данных»
--ЗАДАНИЕ 1
-- Добавление данных в таблицу исполнителей
INSERT INTO artist (artist_name) VALUES
('John Doe'),
('Alice'),
('Bob Smith'),
('Charlie Brown');

-- Добавление данных в таблицу жанров
INSERT INTO genre (genre_name) VALUES
('Pop'),
('Rock'),
('Hip-Hop');

-- Добавление данных в таблицу альбомов
INSERT INTO album (album_name, release_year) VALUES
('Album 1', 2019),
('Album 2', 2020),
('Album 3', 2018);

-- Добавление данных в таблицу артист_жанр
INSERT INTO artist_genre (artist_id, genre_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 1),
(4, 2);

-- Добавление данных в таблицу артист_альбом
INSERT INTO artist_album (artist_id, album_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 1),
(4, 2);

-- Добавление данных в таблицу треков
INSERT INTO track (track_name, duration, album_id) VALUES
('Track 1', 200, 1),
('Track 2-my', 220, 1),
('Track 3', 250, 2),
('Track 4', 180, 2),
('Track 5', 300, 3),
('Track 6', 210, 3);

-- Добавление данных в таблицу сборников
INSERT INTO collection (collection_name, release_year) VALUES
('Collection 1', 2018),
('Collection 2', 2019),
('Collection 3', 2020),
('Collection 4', 2021);

-- Добавление данных в таблицу трек_сборник
INSERT INTO track_in_collection (track_id, collection_id) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 3),
(6, 3);

-- Добавление данных в таблицу исполнителей
INSERT INTO artist (artist_name) VALUES
('Eve'),
('David Bowie');

-- Добавление данных в таблицу артист_жанр
INSERT INTO artist_genre (artist_id, genre_id) VALUES
(5, 1),
(6, 2);

-- Добавление данных в таблицу артист_альбом
INSERT INTO artist_album (artist_id, album_id) VALUES
(5, 2),
(6, 3);

-- Добавление данных в таблицу треков
INSERT INTO track (track_name, duration, album_id) VALUES
('Track 7', 190, 2),
('Track 8', 280, 3);

--Для Задание 4 Наименования треков, которые не входят в сборники.
INSERT INTO track (track_name, duration) VALUES
('Track 9', 290);

-- Добавление данных в таблицу трек_сборник
INSERT INTO track_in_collection (track_id, collection_id) VALUES
(7, 4),
(8, 4);
