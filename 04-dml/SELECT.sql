--ЗАДАНИЕ 2
--Название и продолжительность самого длительного трека
SELECT track_name, duration
FROM track
ORDER BY duration DESC
LIMIT 1;

--Название треков, продолжительность которых не менее 3,5 минут:
SELECT track_name
FROM track
WHERE duration >= 210;-- Трек у меня измеряется в секундах

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно:
SELECT collection_name
FROM collection
WHERE release_year BETWEEN 2018 AND 2020;

--Исполнители, чьё имя состоит из одного слов
SELECT artist_name
FROM artist
WHERE artist_name NOT LIKE '% %'; -- Не содержит пробелов

--Название треков, которые содержат слово «мой» или «my»
SELECT track_name
FROM track
WHERE track_name ILIKE '%мой%' OR track_name ILIKE '%my%';

--ЗАДАНИЕ 3
--Количество исполнителей в каждом жанре
SELECT g.genre_name, COUNT(ag.artist_id) AS artist_count
FROM genre g
LEFT JOIN artist_genre ag ON g.genre_id = ag.genre_id
GROUP BY g.genre_name;

--Количество треков, вошедших в альбомы 2019–2020 годов
SELECT COUNT(track_id) AS track_count
FROM track t
JOIN album a ON t.album_id = a.album_id
WHERE a.release_year BETWEEN 2019 AND 2020;

--Средняя продолжительность треков по каждому альбому.
SELECT a.album_name, AVG(t.duration) AS average_duration
FROM album a
JOIN track t ON a.album_id = t.album_id
GROUP BY a.album_name;

--Все исполнители, которые не выпустили альбомы в 2020 году
SELECT artist_name
FROM artist
WHERE artist_id NOT IN (
    SELECT DISTINCT artist_id
    FROM artist_album
    JOIN album ON artist_album.album_id = album.album_id
    WHERE release_year = 2020
);

--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
SELECT c.collection_name
FROM collection c
JOIN track_in_collection tic ON c.collection_id = tic.collection_id
JOIN track t ON tic.track_id = t.track_id
JOIN album a ON t.album_id = a.album_id
JOIN artist_album aa ON a.album_id = aa.album_id
JOIN artist ar ON aa.artist_id = ar.artist_id
WHERE ar.artist_name = 'Alice';


--ЗАДАНИЕ 4
--Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
SELECT DISTINCT a.album_name
FROM album a
JOIN artist_album aa ON a.album_id = aa.album_id
JOIN artist_genre ag ON aa.artist_id = ag.artist_id
GROUP BY a.album_name
HAVING COUNT(DISTINCT ag.genre_id) > 1;

--Наименования треков, которые не входят в сборники.
SELECT track_name
FROM track t
LEFT JOIN track_in_collection tic ON t.track_id = tic.track_id
WHERE tic.track_id IS NULL;

--Исполнитель или исполнители, написавшие самый короткий по продолжительности трек,
--теоретически таких треков может быть несколько.
SELECT ar.artist_name, t.track_name, t.duration
FROM track t
JOIN artist_album aa ON t.album_id = aa.album_id
JOIN artist ar ON aa.artist_id = ar.artist_id
WHERE t.duration = (
    SELECT MIN(duration)
    FROM track
);
--Названия альбомов, содержащих наименьшее количество треков.
SELECT album_name, COUNT(track_id) AS track_count
FROM album a
LEFT JOIN track t ON a.album_id = t.album_id
GROUP BY album_name
ORDER BY track_count ASC
LIMIT 1;
