CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    category TEXT
);

CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    user_id INTEGER REFERENCES users,
    category_id INTEGER REFERENCES categories,
    sent_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS feedback ( 
    id SERIAL PRIMARY KEY, 
    content TEXT, 
    user_id INTEGER REFERENCES users, 
    sent_at TIMESTAMP
);