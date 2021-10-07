import pymysql
from pymysql import Error
from secret import *


#create connection

# Database Connection
connection = pymysql.connect(host='localhost', user='root', password= passCode, db='employee')

#Cursor Object
Cursor = connection.cursor()

# Select Query
select_query = '''
                SELECT * 
                FROM employee
                WHERE first_name = 'Emeka'
                '''

delete_query = '''
                DELETE FROM employee
                WHERE first_name = 'Emeka'
                '''

try:
    # Print Records
    print('Records before deleting')
    Cursor.execute(select_query)
    record = Cursor.fetchone()
    print(record)

    #Delete Records
    Cursor.execute(delete_query)

    #commit changes
    connection.commit()

    #check if record is deleted
    Cursor.execute(select_query)
    record = Cursor.fetchall()
    if len(record) == 0:
        print('Record deleted successfully')

except Error as e:
    #rollback changes
    connection.rollback()
    print('Error deleting row')

finally:
    #close connection
    connection.close()
    print('Connection is closed')
