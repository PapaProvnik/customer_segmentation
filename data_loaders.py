import pymysql

def truncate_table(db_host, db_user, db_password, db_name, table_name):
    """
    Truncates a table in a MySQL database.

    Parameters:
    db_host (str): The database host.
    db_user (str): The database user.
    db_password (str): The database user's password.
    db_name (str): The name of the database.
    table_name (str): The name of the table to truncate.

    Returns:
    None
    """
    # Establish a database connection
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    try:
        with connection.cursor() as cursor:
            # Execute the TRUNCATE TABLE command
            cursor.execute(f"TRUNCATE TABLE {table_name}")
            # Commit the changes
            connection.commit()
            print(f"Table {table_name} truncated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the database connection
        connection.close()
