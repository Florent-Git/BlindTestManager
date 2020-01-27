import psycopg2 as postgre

try:
    connection = postgre.connect(user="bt_manager", password="blindtestmanager", host="localhost", port="5432", database="blindtestmanager")

    cursor = connection.cursor()

    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, postgre.Error) as error:
    print("Error while connecting to database: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed")
