import psycopg2
from psycopg2 import Error

try:
    #create connection
    connection = psycopg2.connect(host='localhost', user='postgres', password='password', database='university')
   
    #cursor object
    cursor = connection.cursor()

    # drop table if it exists
    cursor.execute('DROP TABLE IF EXISTS student') 

    #query - create table
    query = '''
            CREATE TABLE student 
            (student_id INTEGER PRIMARY KEY NOT NULL,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            age INTEGER)
            '''

    #execute query
    cursor.execute(query)

    #commit changes
    connection.commit()
    
    #print message
    print('Table created successfully')

except Error as e:
    #rollback changes
    connection.rollback()
    print('Error creating table')

finally:
    #close connection
    connection.close()
    print('Connection is closed')