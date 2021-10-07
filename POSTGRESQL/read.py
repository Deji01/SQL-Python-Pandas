import psycopg2
from psycopg2 import Error
'''
READ RECORDS FROM DATABASE
'''
def getActor(name):
    try:
        #create connection
        connection = psycopg2.connect(host='localhost', user='postgres', password='password', database='postgres')
    
        #cursor object
        cursor = connection.cursor() 

        #read query 
        query = '''
                SELECT *
                FROM actor
                WHERE first_name = %s
                '''
        #execute query
        cursor.execute(query,(name,))
        records = cursor.fetchall()

        for row in records:
            print('Actor ID', row[0])
            print('First Name', row[1])
            print('Last Name', row[2])
            print('Last Update', row[3], '\n')

    except Error as e:
        print('Error reading records')

    finally:
        #close connection
        connection.close()
        print('Connection is closed')

getActor('James')
