import pymysql.cursors
import time
connection = pymysql.connect(host='192.168.0.5',
                             user='DBA',
                             password='xxx',
                             database='testdb01',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def Update_Mysql(connection,querie):
    with connection:
        with connection.cursor() as cursor:
            connection.ping()
            cursor.execute(querie)
            result = connection.commit()
    return result
    connection.close()

def Select_Mysql(connection,querie):
    with connection.cursor() as cursor:
        connection.ping()
        cursor.execute(querie)
        result = cursor.fetchall()
    return result
    connection.close()


print("Creating the DB")
querie = "CREATE TABLE dogs(name varchar(40), age INT, breed varchar(40));"
print(Update_Mysql(connection,querie))
time.sleep(2)

print('Checking table')
querie = " show tables;"
print(Select_Mysql(connection,querie))

print('Insert data')
querie = "INSERT INTO dogs VALUES ('star','8','Labrador');"
Update_Mysql(connection,querie)

querie = "INSERT INTO dogs VALUES ('ski','9','Cat');"
Update_Mysql(connection,querie)

querie = "INSERT INTO dogs VALUES ('pofi','11','Podel');"
Update_Mysql(connection,querie)

print('checking the data')
querie = "SELECT * FROM dogs;"
result =Select_Mysql(connection,querie)
for x in result:
    print(x)

print('Im updating')
querie = "UPDATE dogs SET age = 10 WHERE name = 'star';"
Update_Mysql(connection,querie)

print('checking')
querie ="SELECT age FROM dogs where name='star';"
print(Select_Mysql(connection,querie))

print('Delete pofi')
querie = "DELETE FROM dogs WHERE name='pofi'; "
Update_Mysql(connection,querie)

print('Print DATA')
querie ="SELECT * FROM dogs;"
print(Select_Mysql(connection,querie))