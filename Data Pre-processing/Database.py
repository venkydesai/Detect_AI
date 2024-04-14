import sys

# Appending the credentials path
sys.path.append('../')
from credentials import credentials

# Function to connect to mySQL Server
def connectToServer(host_name: str, username: str, pwd: str):
    connection = None

    # Trying to connect to the server
    try:
        connection = mysql.connector.connect(
            user=username,
            password=pwd,
            host=host_name
        )
        # Printing here to make sure that the server was connected to properly
        print('Connected to Server!')
    except Error as err:
        print('Error Occured in Connecting to Database:')
        print(f'{err}')
    
    # Returning the connection
    return connection

# A function to create the database
def create_database(server_connection, database_name: str):
    """
    create_database

    A function to create the database

    inputs:
    server_connection -> an object representing the connection to the server
    database_name -> a string for the database name

    outputs:
    None
    """
    cursor = server_connection.cursor()
    query = f'CREATE DATABASE {database_name}'

    # Executing the query
    try:
        cursor.execute(query)
        print('Database created successfully')
    except Error as err:
        print('Problem in Database Creation:')
        print(err)

# A function to connect to the database
def create_db_connection(host_name:str, user_name:str, password:str, db_name:str):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=password,
            database=db_name
        )
        print(f"Connected to {db_name} Successfully")
    except Error as err:
        print('Error in Database Connection:')
        print(f"Error: '{err}'")
    return connection

# A function to execute queries
def modify_queries(query:str,connection):
    cursor = connection.cursor()

    # Trying to execute the query
    try:
        cursor.execute(query)
        connection.commit()
        print('Query ran')
    except Error as err:
        print('Query caused an error:')
        print(err)

# A function to other queries such as searching, etc
def querying(query:str, connection):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# Main Method
if __name__ == '__main__':
    # Setting up the connection to the server
    server_connection = connectToServer(host_name=credentials['host'],
                                        username=credentials['user'],pwd=credentials['password'])

    # Creating the database
    create_database(server_connection,'AuthenticAI')

    # Create connection to database
    database_connection = create_db_connection(credentials['host'],
                                        credentials['user'],credentials['password'],'AuthenticAI')
    
    # Creating the table 
    create_table = modify_queries(create_table,database_connection)
    
    # Closing database connection
    database_connection.close()

    # Closing server connection
    server_connection.close()