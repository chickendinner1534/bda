import sqlite3
import pandas as pd

# Connect to in-memory SQLite DB
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a sales table
cursor.execute('''
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

# Insert sample sales data
sales_data = [
    (1, 'Laptop', 1, 1000.0),
    (1, 'Mouse', 2, 25.0),
    (2, 'Laptop', 1, 950.0),
    (3, 'Keyboard', 1, 75.0),
    (2, 'Mouse', 1, 25.0),
    (3, 'Laptop', 2, 1000.0),
]

cursor.executemany('INSERT INTO sales (customer_id, product, quantity, price) VALUES (?, ?, ?, ?)', sales_data)
conn.commit()

# Aggregation Queries
print("Total number of sales:", cursor.execute('SELECT COUNT(*) FROM sales').fetchone()[0])
print("Total quantity sold:", cursor.execute('SELECT SUM(quantity) FROM sales').fetchone()[0])
print("Average price:", cursor.execute('SELECT AVG(price) FROM sales').fetchone()[0])
print("Minimum price:", cursor.execute('SELECT MIN(price) FROM sales').fetchone()[0])
print("Maximum price:", cursor.execute('SELECT MAX(price) FROM sales').fetchone()[0])

# GROUP BY product - total quantity and total revenue by product
group_by_query = '''
SELECT product, SUM(quantity) as total_quantity, SUM(quantity * price) as total_revenue
FROM sales
GROUP BY product
'''
df_group = pd.read_sql(group_by_query, conn)
print("\nAggregated sales by product:")
print(df_group)
