import sqlite3
import pandas as pd

# Connect to in-memory SQLite DB
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a 'users' table (like a collection for user data)
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    age INTEGER,
    city TEXT
)
''')

# Insert documents (records) into the collection
users = [
    ('Alice', 'alice@example.com', 28, 'New York'),
    ('Bob', 'bob@example.com', 22, 'Los Angeles'),
    ('Charlie', 'charlie@example.com', 35, 'Chicago'),
    ('Diana', 'diana@example.com', 27, 'San Francisco'),
]
cursor.executemany('INSERT INTO users (name, email, age, city) VALUES (?, ?, ?, ?)', users)
conn.commit()

# Fetch documents based on criteria (e.g., age > 25)
print("Users with age > 25:")
print(pd.read_sql('SELECT * FROM users WHERE age > 25', conn))

# Modify existing records (e.g., update age for Bob)
cursor.execute('UPDATE users SET age = 23 WHERE name = "Bob"')
conn.commit()

# Verify update
print("\nAfter updating Bob's age:")
print(pd.read_sql('SELECT * FROM users WHERE name = "Bob"', conn))

# Remove documents from the collection (e.g., delete user Diana)
cursor.execute('DELETE FROM users WHERE name = "Diana"')
conn.commit()

# Verify delete
print("\nAfter deleting Diana:")
print(pd.read_sql('SELECT * FROM users', conn))
