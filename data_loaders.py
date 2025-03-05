import pymysql
import pandas as pd
from sqlalchemy import create_engine

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
    with connection.cursor() as cursor:
        # Execute the TRUNCATE TABLE command
        cursor.execute(f"TRUNCATE TABLE {table_name}")
        # Commit the changes
        connection.commit()
        print(f"Table {table_name} truncated successfully.")

    # Close the database connection
    connection.close()

def upload_df_to_sql(df, table_name, db_url):
    """
    Uploads a DataFrame to an SQL database.

    Parameters:
    df (pd.DataFrame): The DataFrame to upload.
    table_name (str): The name of the table to upload the DataFrame to.
    db_url (str): The database URL in the format 'dialect+driver://username:password@host:port/database'.

    Returns:
    None
    """
    engine = create_engine(db_url)

    # Upload the DataFrame to the specified table
    df_no_header = df.iloc[1:]
    df_no_header.to_sql(name=table_name, con=engine, if_exists='append', index=False)

    print(f"DataFrame uploaded to {table_name} table.")