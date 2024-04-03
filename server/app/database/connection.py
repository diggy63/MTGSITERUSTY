import psycopg2

def connect_to_psql():
    try:
        connection = psycopg2.connect(
            user="diggy",
            password="",
            host="localhost",
            port="5432",
            database="mtgjson"
        )
        print("Connection to PostgreSQL successful")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None