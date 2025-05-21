import sqlite3
import pandas as pd
import uuid

# Connect to in-memory SQLite DB (simulate Cassandra keyspace and table)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Simulate keyspace by just naming the database logically in comments
# Create table 'users' with UUID as PRIMARY KEY (string in SQLite)
cursor.execute('''
CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    name TEXT,
    email TEXT,
    age INTEGER
)
''')

# Insert records (simulate UUIDs)
users = [
    (str(uuid.uuid4()), 'Alice', 'alice@example.com', 30),
    (str(uuid.uuid4()), 'Bob', 'bob@example.com', 25)
]
cursor.executemany('INSERT INTO users (user_id, name, email, age) VALUES (?, ?, ?, ?)', users)
conn.commit()

# Query records
print("Users:")
df = pd.read_sql('SELECT * FROM users', conn)
print(df)

# Update a record (update Alice's age)
alice_id = df[df['name']=='Alice']['user_id'].values[0]
cursor.execute('UPDATE users SET age = ? WHERE user_id = ?', (31, alice_id))
conn.commit()

# Delete a record (delete Bob)
bob_id = df[df['name']=='Bob']['user_id'].values[0]
cursor.execute('DELETE FROM users WHERE user_id = ?', (bob_id,))
conn.commit()

# Final data after update and delete
print("\nUsers after update and delete:")
df_final = pd.read_sql('SELECT * FROM users', conn)
print(df_final)
