import psycopg2
from psycopg2 import Error

try:
    #create connection
    connection = psycopg2.connect(host='localhost', user='postgres', password= 'password', database='university')

    #cursor object
    cursor = connection.cursor() 

    #query - insert
    query = '''
            INSERT INTO student (student_id, first_name, last_name , age )
            VALUES (1, 'Emeka','Frank',24)
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
