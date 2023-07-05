import psycopg2


connection = None
host = "localhost"
user = "admin"
password = "admin"
port = "5432"
db_name = "postgres"
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=db_name
    )
    # connection.autocommit() = True

    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Select version: {cursor.fetchone()}")
    # Create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
            id serial PRIMARY KEY,
            first_name varchar(50) NOT NULL
            nick_name varchar(50) NOT NULL);
            """
        )
        # connection.commit()
        print("[INFO] Table created successfully")
except Exception as ex:
    print("[INFO] ERROR while working with PostgreSQL", ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
