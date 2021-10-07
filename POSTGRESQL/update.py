import psycopg2
from psycopg2 import Error

try:
    #create connection
    connection = psycopg2.connect(host='localhost', user='postgres', password='password', database='university')
   
    #cursor object
    cursor = connection.cursor() 

    #query - update
    query = '''
            UPDATE student 
            SET age = 27
            '''
    #execute query
    cursor.execute(query)

    #commit changes
    connection.commit()

    #check for update
    cursor.execute('''
                    SELECT *
                    FROM student
                    ''')
    records = cursor.fetchall()
    for row in records:
        print('Student ID', row[0])
        print('First Name', row[1])
        print('Last Name', row[2])
        print('Age', row[3], '\n')
    
    #print message
    print('Successful update')

except Error as e:
    #rollback changes
    connection.rollback()
    print('Error Updating')

finally:
    #close connection
    connection.close()
    print('Connection is closed')
