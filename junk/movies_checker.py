import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('test.db')

try:
    # Create a cursor object
    cursor = conn.cursor()

    # # Create a table if it doesn't exist
    # cursor.execute("CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, name TEXT)")

    # # Insert some data into the table
    # cursor.execute("INSERT INTO my_table (name) VALUES ('John')")
    # cursor.execute("INSERT INTO my_table (name) VALUES ('Alice')")

    # # Commit changes
    # conn.commit()

    # Retrieve data from the table
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()

    # Print the retrieved data
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    # Close connection
    conn.close()
