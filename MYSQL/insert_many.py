import pymysql
from pymysql import Error
from secret import *


#create connection

# Database Connection
connection = pymysql.connect(host='localhost', user='root', password= passCode, db='employee')

#cursor object
cursor = connection.cursor() 

#query - insert
query = '''
        INSERT INTO employee (first_name, last_name , age , salary)
        VALUES (%s, %s, %s, %s)
        '''

#create insert list
records = [(('Akatugba', 'Saviour', 15, 35000)),
            ('Ayodeji', 'Bolt', 35, 25000),
                ('Ahmed', 'Musa', 20, 5000),
            ]

try:
    #execute query
    cursor.executemany(query, records)

    #commit changes
    connection.commit()
    
    #print message
    print(cursor.rowcount, 'records inserted')

except Error as e:
    #rollback changes
    connection.rollback()
    print('Error inserting rows')

finally:
    #close connection
    connection.close()
    print('Connection is closed')
