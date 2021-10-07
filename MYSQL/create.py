# Import Libraries
import pymysql
from secret import *
from pymysql import Error

try:
    # Database Connection
    connection = pymysql.connect(
                host='localhost', user='root', password= passCode, db='employee'
    )

    #Cursor Object
    Cursor = connection.cursor()

    #Drop Table if Exists
    Cursor.execute('DROP TABLE IF EXISTS employee')

    # Create Table
    query = '''
            CREATE TABLE employee (
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20),
            age INTEGER,
            salary FLOAT
            )
            '''

    # Execute Query
    Cursor.execute(query)

    #commit changes
    connection.commit()
    
    #print message
    print('Table Created successfully')

except Error as e:
    #rollback changes
    connection.rollback()
    print('Error Creating Table')

finally:
    #close connection
    connection.close()
    print('Connection is closed')