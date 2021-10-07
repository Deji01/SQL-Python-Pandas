import pymysql
from pymysql import Error
from secret import *


#create connection

# Database Connection
connection = pymysql.connect(host='localhost', user='root', password= passCode, db='employee')

#cursor object
cursor = connection.cursor() 

#query - update
query = '''
        UPDATE employee
        SET salary =  %s
        WHERE first_name = %s
        '''

try:
    records = [(15000, 'Emeka'), (40000, 'Akatugba')]
    #execute query
    cursor.executemany(query, records)

    #commit changes
    connection.commit()
    
    #print message
    print(cursor.rowcount, 'rows updated')

except Error as e:
    #rollback changes
    connection.rollback()
    print('Error inserting record')

finally:
    #close connection
    connection.close()
    print('Connection is closed')
