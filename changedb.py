import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Retrieve data from the table
# Fetch movies and store in a dictionary
cursor.execute("SELECT * FROM movies")
conn.commit()