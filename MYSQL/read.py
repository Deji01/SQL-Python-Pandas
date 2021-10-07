import pymysql
from pymysql import Error
from secret import *


#create connection

# Database Connection
connection = pymysql.connect(host='localhost', user='root', password= passCode, db='employee')

#cursor object
cursor = connection.cursor() 

#query - select
query = '''
        SELECT *
        FROM employee
        '''

try:
    #execute query
    cursor.execute(query)
    records = cursor.fetchall()
    print(cursor.rowcount, 'total rows', '\n')

    for row in records:
        print('First Name', row[0])
        print('Last Name', row[1])
        print('Age', row[2])
        print('Salary', row[3], '\n')

except Error as e:
    print('Error fetching rows')

finally:
    #close connection
    connection.close()
    print('Connection is closed')


