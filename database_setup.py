import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INTEGER,
    Hire_Date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Manager TEXT
)
""")

cursor.executemany("INSERT INTO Employees VALUES (?, ?, ?, ?, ?)", [
    (1, 'Alice', 'Sales', 50000, '2021-01-15'),
    (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
    (3, 'Charlie', 'Marketing', 60000, '2022-03-20')
])

cursor.executemany("INSERT INTO Departments VALUES (?, ?, ?)", [
    (1, 'Sales', 'Alice'),
    (2, 'Engineering', 'Bob'),
    (3, 'Marketing', 'Charlie')
])

conn.commit()
conn.close()

print("created")
