import pymysql.cursors
import random

connection = pymysql.connect(host='192.168.0.5',
                             user='DBA',
                             password='Gg442875',
                             database='testdb01',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# with connection.cursor() as cursor:
#     # Read a single record
#     sql = "SELECT * FROM pet;"
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     print(result)

# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO pet VALUES ('start','guy','lavrador','f','1999-03-30',NULL);"
#         cursor.execute(sql)
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "UPDATE pet SET name = 'star' WHERE owner = 'guy';"
#         cursor.execute(sql)
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()


# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "CREATE TABLE dogs(name varchar(40), age INT, breed varchar(40));"
#         cursor.execute(sql)
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

print(random.randint(1,1000))