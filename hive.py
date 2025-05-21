import sqlite3
import pandas as pd

# Create in-memory SQLite DB
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create tables
cursor.execute("CREATE TABLE customers (cust_id INT, age INT, name TEXT, address TEXT, salary REAL)")
cursor.execute("CREATE TABLE orders (order_id INT, date TEXT, cust_id INT, amount REAL)")

# Insert sample data
cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?)", [
    (1, 25, 'Alice', 'NY', 50000),
    (2, 30, 'Bob', 'CA', 60000),
    (3, 22, 'Charlie', 'TX', 45000),
    (4, 28, 'David', 'NV', 52000)
])

cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", [
    (101, '2023-01-01', 1, 200),
    (102, '2023-01-02', 1, 150),
    (103, '2023-01-03', 2, 300),
    (104, '2023-01-04', 5, 500)  # customer id 5 doesn't exist
])
print(pd.read_sql_query("SELECT * FROM customers", conn))
print(pd.read_sql_query("SELECT * FROM orders", conn))
# Perform JOINs
print("\nINNER JOIN:")
df = pd.read_sql_query("""
SELECT c.cust_id, c.name, o.order_id, o.amount
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
""", conn)
print(df)

print("\nLEFT JOIN:")
df = pd.read_sql_query("""
SELECT c.cust_id, c.name, o.order_id, o.amount
FROM customers c
LEFT JOIN orders o ON c.cust_id = o.cust_id
""", conn)
print(df)

print("\nRIGHT JOIN (simulated using LEFT JOIN):")
df = pd.read_sql_query("""
SELECT o.cust_id, c.name, o.order_id, o.amount
FROM orders o
LEFT JOIN customers c ON c.cust_id = o.cust_id
""", conn)
print(df)

print("\nFULL OUTER JOIN (simulated using UNION):")
df = pd.read_sql_query("""
SELECT c.cust_id, c.name, o.order_id, o.amount
FROM customers c
LEFT JOIN orders o ON c.cust_id = o.cust_id
UNION
SELECT o.cust_id, c.name, o.order_id, o.amount
FROM orders o
LEFT JOIN customers c ON c.cust_id = o.cust_id
""", conn)
print(df)

conn.close()
