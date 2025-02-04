import sqlite3

#cerate database
connection = sqlite3.connect("student.db")

#create cursor
cursor = connection.cursor()

create_table_query = """
    CREATE TABLE IF NOT EXISTS STUDENT(
        NAME VARCHAR(25),
        COURSE VARCHAR(25),
        SECTION VARCHAR(25),
        MARKS INT
    );
"""

cursor.execute(create_table_query)

# Insert Records

sql_query = " INSERT INTO STUDENT (NAME, COURSE, SECTION, MARKS) VALUES (?,?,?,?)"
values = [
    ('student1', 'data science', 'A', 90),
    ('student2', 'data science', 'A', 70),
    ('student3', 'science', 'B', 90),
    ('student4', 'Machine Learning', 'B', 80)    
]

cursor.executemany(sql_query, values)
connection.commit()

data = cursor.execute(""" select * from STUDENT """)

for row in data:
    print(row)

if connection:
    connection.close()
