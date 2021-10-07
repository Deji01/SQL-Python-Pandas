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
    fetch_size = 3
    records = cursor.fetchmany(fetch_size)

    print(cursor.rowcount, 'total rows')

    print('Each record')
    
    for row in records:
        print(row)
        

except Error as e:
    print('Error fetching row')

finally:
    #close connection
    connection.close()
    print('Connection is closed')


