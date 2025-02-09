CREATE TABLE users
(
    id SERIAL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT UNIQUE,
    PRIMARY KEY (id)
);

