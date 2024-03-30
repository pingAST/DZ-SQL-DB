--Создание таблицы исполнителей
CREATE TABLE if not exists artist (
    artist_id SERIAL PRIMARY KEY,
    artist_name VARCHAR(100)
);

-- Создание таблицы жанров:
CREATE TABLE if not exists genre (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(50)
);

-- Создание таблицы альбомов:
CREATE TABLE if not exists album (
    album_id SERIAL PRIMARY KEY,
    album_name VARCHAR(100),
    release_year INTEGER
);

-- Создание таблицы связи между исполнителями и жанрами:
CREATE TABLE if not exists artist_genre (
    artist_id INTEGER REFERENCES artist(artist_id),
    genre_id INTEGER REFERENCES genre(genre_id),
    PRIMARY KEY (artist_id, genre_id)
);

-- Создание таблицы связи между исполнителями и альбомами
CREATE TABLE if not exists artist_album (
    artist_id INTEGER REFERENCES artist(artist_id),
    album_id INTEGER REFERENCES album(album_id),
    PRIMARY KEY (artist_id, album_id)
);

-- Создание таблицы треков:
CREATE TABLE if not exists track (
    track_id SERIAL PRIMARY KEY,
    track_name VARCHAR(100),
    duration INTEGER,
    album_id INTEGER REFERENCES album(album_id)
);

-- Создание таблицы сборников:
CREATE TABLE if not exists collection (
    collection_id SERIAL PRIMARY KEY,
    collection_name VARCHAR(100),
    release_year INTEGER
);

--Создание таблицы "трек в сборнике":
CREATE TABLE if not exists track_in_collection (
    track_id INTEGER REFERENCES track(track_id),
    collection_id INTEGER REFERENCES collection(collection_id),
    PRIMARY KEY (track_id, collection_id)
);
