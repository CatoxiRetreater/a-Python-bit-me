import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

with open('input.txt', 'r') as file:
    data = file.read()

cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", (data, 25))

conn.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
