import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Customers table (larger entity)
cursor.execute('''
CREATE TABLE customers (
    cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
''')

# Orders table with embedded shipping address (small embedded doc) and customer reference
cursor.execute('''
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cust_id INTEGER,
    order_date TEXT,
    shipping_address TEXT,
    shipping_city TEXT,
    shipping_zip TEXT
)
''')

conn.commit()

# Insert customers
customers = [('Alice Smith', 'alice@example.com'), ('Bob Johnson', 'bob@example.com')]
cursor.executemany('INSERT INTO customers (name, email) VALUES (?, ?)', customers)

# Insert orders with embedded shipping address and customer references
orders = [
    (1, '2025-05-21', '123 Main St', 'New York', '10001'),
    (1, '2025-05-23', '123 Main St', 'New York', '10001'),
    (2, '2025-05-22', '456 Oak Ave', 'Los Angeles', '90001'),
]
cursor.executemany('INSERT INTO orders (cust_id, order_date, shipping_address, shipping_city, shipping_zip) VALUES (?, ?, ?, ?, ?)', orders)

conn.commit()

# Query: fetch all orders for a specific customer (cust_id=1)
customer_id = 1
cursor.execute('SELECT * FROM orders WHERE cust_id = ?', (customer_id,))
orders_for_customer = cursor.fetchall()

print(f"Orders for customer_id={customer_id}:")
for order in orders_for_customer:
    print(order)
