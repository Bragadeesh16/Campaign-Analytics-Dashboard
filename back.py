import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


try:
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    print("Connected to the database.")

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS company_list (
            id SERIAL PRIMARY KEY, 
            company_name VARCHAR(255), 
            status VARCHAR(50), 
            clicks INT, 
            cost DECIMAL, 
            impressions INT
        )
    """)

    print("Table created successfully.")

    # Insert data into the table
    insert_query = """INSERT INTO company_list (google, active, 100, 1200, 200)
                      VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(insert_query)
    connection.commit()
    print("Data inserted successfully.")

    # Retrieve and print all rows from the table
    cursor.execute("SELECT * FROM company_list")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")
