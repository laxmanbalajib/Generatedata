import time
import mysql.connector
import datetime
import requests
import random
import json


with open('MOCK_DATA.json') as json_file:
    data = json.load(json_file)


# establishing the connection
conn = mysql.connector.connect(
    user='root', password='password', host='127.0.0.1', database='schoolSystems'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()
cursor.execute("DROP TABLES Earn, Staff, TuitionFee, Attend, Teach, Course")
# for testing purposes
cursor.execute("DROP TABLE IF EXISTS Staff")

stmt = "SHOW TABLES LIKE 'Staff'"
cursor.execute(stmt)
result = cursor.fetchone()
# Dropping SiteData table if already exists.
if result is None:

    # Creating table as per requirement
    sql = '''CREATE TABLE Staff(
    id INT NOT NULL,
    name CHAR(50) NOT NULL,
    gender CHAR(10) NOT NULL,
    PRIMARY KEY (id)
    )'''
    cursor.execute(sql)

# Preparing SQL query to INSERT a record into the database.
sql = '''INSERT INTO Staff(id, name, gender)VALUES (%s, %s, %s)'''

staffIdList = []

for staff in data:
    print(staff["name"])
    staffIdList.append(staff["id"])
    try:
        # Executing the SQL command
        cursor.execute(
            sql, (staff["id"], staff["name"], staff["gender"]))

        # Commit your changes in the database
        conn.commit()

        print("Inserted into Table")
    except:
        # Rolling back in case of error
        conn.rollback()
        print("SQL Error")

print("\n Staff table has been created and populated....\n")

conn.close


# establishing the connection
conn = mysql.connector.connect(
    user='root', password='password', host='127.0.0.1', database='schoolSystems'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# for testing purposes
cursor.execute("DROP TABLE IF EXISTS Course")

stmt = "SHOW TABLES LIKE 'Course'"
cursor.execute(stmt)
result = cursor.fetchone()
# Dropping SiteData table if already exists.
if result is None:

    # Creating table as per requirement
    sql = '''CREATE TABLE Course(
    courseNumber CHAR(10) NOT NULL,
    courseName CHAR(60) NOT NULL,
    courseFee int NOT NULL,
    PRIMARY KEY (courseNumber)
    )'''
    cursor.execute(sql)

# Preparing SQL query to INSERT a record into the database.
sql = '''INSERT INTO Course(courseNumber, courseName, courseFee)VALUES (%s, %s, %s)'''

courseNumberList = ["CSCE601", "CSCE603", "CSCE604", "CSCE605", "CSCE606"]
courseNameList = ["Programming with C and Java",
                  "Database Systems and Applications", "Programming Languages", "Compiler Design", "Software Engineering"]
courseFee = [1800, 2000, 2200, 2400, 1900]

for i in range(0, len(courseNameList)):
    try:
        # Executing the SQL command
        cursor.execute(
            sql, (courseNumberList[i], courseNameList[i], random.choice(courseFee)))

        # Commit your changes in the database
        conn.commit()

        print("Inserted into Table")
    except:
        # Rolling back in case of error
        conn.rollback()
        print("SQL Error")

print("\n Course table has been created and populated....\n")

conn.close


# establishing the connection
conn = mysql.connector.connect(
    user='root', password='password', host='127.0.0.1', database='schoolSystems'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# for testing purposes
cursor.execute("DROP TABLE IF EXISTS Teach")

stmt = "SHOW TABLES LIKE 'Teach'"
cursor.execute(stmt)
result = cursor.fetchone()
# Dropping SiteData table if already exists.
if result is None:

    # Creating table as per requirement
    sql = '''CREATE TABLE Teach(
    courseNumber CHAR(10) NOT NULL,
    staffId INT NOT NULL,
    FOREIGN KEY (courseNumber) REFERENCES Course(courseNumber) ON DELETE CASCADE,
    FOREIGN KEY (staffId) REFERENCES Staff(id) ON DELETE CASCADE
    )'''
    cursor.execute(sql)


# Preparing SQL query to INSERT a record into the database.
sql = '''INSERT INTO Teach(courseNumber, staffId) VALUES (%s, %s)'''

courseNumberList = ["CSCE601", "CSCE603", "CSCE604", "CSCE605", "CSCE606"]

count = 0

while count < 20:
    staffId = random.choice(staffIdList)
    courseNumber = random.choice(courseNumberList)

    stmt = "SELECT * FROM Teach WHERE courseNumber = (%s) AND staffId = (%s)"
    cursor.execute(stmt, (courseNumber, staffId))
    result = cursor.fetchone()

    if result != None:
        continue

    try:
        # Executing the SQL command
        cursor.execute(
            sql, (courseNumber, staffId))

        # Commit your changes in the database
        conn.commit()

        print("Inserted into Table")
    except:
        # Rolling back in case of error
        conn.rollback()
        print("SQL Error")
    count += 1

print("\n Teach table has been created and populated....\n")

conn.close

# establishing the connection
conn = mysql.connector.connect(
    user='root', password='password', host='127.0.0.1', database='schoolSystems'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# for testing purposes
cursor.execute("DROP TABLE IF EXISTS Earn")

stmt = "SHOW TABLES LIKE 'Earn'"
cursor.execute(stmt)
result = cursor.fetchone()
# Dropping SiteData table if already exists.
if result is None:

    # Creating table as per requirement
    sql = '''CREATE TABLE Earn(
    staffId INT NOT NULL,
    salary INT NOT NULL,
    FOREIGN KEY (staffId) REFERENCES Staff(id) ON DELETE CASCADE
    )'''
    cursor.execute(sql)


# Preparing SQL query to INSERT a record into the database.
sql = '''INSERT INTO Earn(staffId, salary) VALUES (%s, %s)'''

salaryList = [126000, 285200, 145600, 191000, 228900]

count = 0

for staffId in staffIdList:
    salary = random.choice(salaryList)
    try:
        # Executing the SQL command
        cursor.execute(
            sql, (staffId, salary))

        # Commit your changes in the database
        conn.commit()

        print("Inserted into Table")
    except:
        # Rolling back in case of error
        conn.rollback()
        print("SQL Error")
    count += 1

print("\n Earn table has been created and populated....\n")

conn.close


with open('student_mock.json') as json_file:
    data = json.load(json_file)


# establishing the connection
conn = mysql.connector.connect(
    user='root', password='password', host='127.0.0.1', database='schoolSystems'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# for testing purposes
cursor.execute("DROP TABLE IF EXISTS Student")

stmt = "SHOW TABLES LIKE 'Student'"
cursor.execute(stmt)
result = cursor.fetchone()
# Dropping SiteData table if already exists.
if result is None:

    # Creating table as per requirement
    sql = '''CREATE TABLE Student(
    id INT NOT NULL,
    name CHAR(50) NOT NULL,
    gender CHAR(10) NOT NULL,
    PRIMARY KEY (id)
    )'''
    cursor.execute(sql)

# Preparing SQL query to INSERT a record into the database.
sql = '''INSERT INTO Student(id, name, gender)VALUES (%s, %s, %s)'''

studentIdList = []

for student in data:
    print(student["name"])
    studentIdList.append(student["id"].replace("-", ""))
    try:
        # Executing the SQL command
        cursor.execute(
            sql, (student["id"].replace("-", ""), student["name"], student["gender"]))

        # Commit your changes in the database
        conn.commit()

        print("Inserted into Table")
    except:
        # Rolling back in case of error
        conn.rollback()
        print("SQL Error")

print("\n Student table has been created and populated....\n")

conn.close


# establishing the connection
conn = mysql.connector.connect(
    user='root', password='password', host='127.0.0.1', database='schoolSystems'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# for testing purposes
cursor.execute("DROP TABLE IF EXISTS Attend")

stmt = "SHOW TABLES LIKE 'Attend'"
cursor.execute(stmt)
result = cursor.fetchone()
# Dropping SiteData table if already exists.
if result is None:

    # Creating table as per requirement
    sql = '''CREATE TABLE Attend(
    courseNumber CHAR(10) NOT NULL,
    studentId INT NOT NULL,
    FOREIGN KEY (courseNumber) REFERENCES Course(courseNumber) ON DELETE CASCADE,
    FOREIGN KEY (studentId) REFERENCES Student(id) ON DELETE CASCADE
    )'''
    cursor.execute(sql)


# Preparing SQL query to INSERT a record into the database.
sql = '''INSERT INTO Attend(courseNumber, studentId) VALUES (%s, %s)'''

courseNumberList = ["CSCE601", "CSCE603", "CSCE604", "CSCE605", "CSCE606"]

count = 0

while count < 80:
    staffId = random.choice(studentIdList)
    courseNumber = random.choice(courseNumberList)

    stmt = "SELECT * FROM Attend WHERE courseNumber = (%s) AND studentId = (%s)"
    cursor.execute(stmt, (courseNumber, staffId))
    result = cursor.fetchone()

    if result != None:
        continue

    try:
        # Executing the SQL command
        cursor.execute(
            sql, (courseNumber, staffId))

        # Commit your changes in the database
        conn.commit()

        print("Inserted into Table")
    except:
        # Rolling back in case of error
        conn.rollback()
        print("SQL Error")
    count += 1

print("\n Attend table has been created and populated....\n")

conn.close


# establishing the connection
conn = mysql.connector.connect(
    user='root', password='password', host='127.0.0.1', database='schoolSystems'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# for testing purposes
cursor.execute("DROP TABLE IF EXISTS TuitionFee")

stmt = "SHOW TABLES LIKE 'TuitionFee'"
cursor.execute(stmt)
result = cursor.fetchone()
# Dropping SiteData table if already exists.
if result is None:

    # Creating table as per requirement
    sql = '''CREATE TABLE TuitionFee(
    studentId INT NOT NULL,
    tuition INT NOT NULL,
    paid CHAR(6) NOT NULL,
    FOREIGN KEY (studentId) REFERENCES Student(id) ON DELETE CASCADE
    )'''
    cursor.execute(sql)


# Preparing SQL query to INSERT a record into the database.
sql = '''INSERT INTO TuitionFee(studentId, tuition, paid) VALUES (%s, %s, %s)'''
findTuition = "SELECT SUM(courseFee) FROM Course, Attend  WHERE Attend.courseNumber = Course.courseNumber AND Attend.studentId = (%s)"
tuitionList = [12400, 8000, 4500, 14000, 7800]
paidList = ["True", "False"]

count = 0

for studentId in studentIdList:
    cursor.execute(findTuition, (studentId,))
    tuition = int(cursor.fetchone()[0])
    paid = random.choice(paidList)

    try:
        # Executing the SQL command
        cursor.execute(
            sql, (studentId, tuition, paid))

        # Commit your changes in the database
        conn.commit()

        print("Inserted into Table")
    except:
        # Rolling back in case of error
        conn.rollback()
        print("SQL Error")
    count += 1

print("\n TutionFee table has been created and populated....\n")

conn.close
