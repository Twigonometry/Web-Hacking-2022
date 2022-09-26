DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username STRING NOT NULL,
    password STRING NOT NULL
);
insert into users values (1, "admin", "b5c8737eaf2e2e52bec770d83f1e9b06");

DROP TABLE IF EXISTS comments;
CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment STRING NOT NULL,
    userid STRING NOT NULL
);