import pymysql
from pymysql import Error
from secret import *

try:
    #create connection
    
    # Database Connection
    connection = pymysql.connect(host='localhost', user='root', password= passCode, db='employee')

    #cursor object
    cursor = connection.cursor() 

    #query - insert
    query = '''
            INSERT INTO employee (first_name, last_name , age , salary)
            VALUES ('Emeka','Okorocha', 28, 45000)
            '''
    #execute query
    cursor.execute(query)

    #commit changes
    connection.commit()
    
    #print message
    print('Record inserted successfully')

except Error as e:
    #rollback changes
    connection.rollback()
    print('Error inserting record')

finally:
    #close connection
    connection.close()
    print('Connection is closed')
