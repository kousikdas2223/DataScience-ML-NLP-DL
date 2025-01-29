
import sqlite3 as sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

# Create a table
cursor.execute('''CREATE TABLE if not exists employee
                  (
                    employee_id integer PRIMARY KEY,
                    employee_name text,
                    employee_designation text,
                    employee_salary Real,
                    employee_dob datetime
                )''')

# Insert a row of data
cursor.execute("INSERT INTO employee VALUES ('10002','Rahul Trivedi','Manager',70500.00,'1980-01-25')")

# Save (commit) the changes
connection.commit()

# Query the database
cursor.execute("SELECT * FROM employee")
results = cursor.fetchall()
for row in results:
    print(row)

# Update a row of data
cursor.execute("UPDATE employee SET employee_salary = 80000.00 WHERE employee_id = 10002")
connection.commit()

# Query the database again to verify the changes
cursor.execute("SELECT * FROM employee")
results = cursor.fetchall()
for row in results:
    print(row)

# Delete a row of data
cursor.execute("DELETE FROM employee WHERE employee_id = 10002")
connection.commit()

# Query the database again to verify the changes
cursor.execute("SELECT * FROM employee")
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor
cursor.close()

# Commit the changes and close the connection
connection.commit()

# Close the connection
connection.close()

# Entering multiple data at same time
connection = sqlite3.connect('example.db')

cursor = connection.cursor()

# Create a table
cursor.execute('''CREATE TABLE if not exists employee
                  (
                    employee_id integer PRIMARY KEY,
                    employee_name text,
                    employee_designation text,
                    employee_salary Real,
                    employee_dob datetime
                )''')

# Insert multiple rows of data

data = [('10003','John Doe','Developer',65000.00,'1985-05-15'),
        ('10004','Jane Smith','Designer',55000.00,'1990-12-31')]

cursor.executemany("INSERT INTO employee VALUES (?,?,?,?,?)", data)

# Save (commit) the changes
connection.commit()

# Query the database
cursor.execute("SELECT * FROM employee")
results = cursor.fetchall()
for row in results:
    print(row)
    

