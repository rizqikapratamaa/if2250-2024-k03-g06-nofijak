import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Commit changes
conn.commit()

# Retrieve data from the table
# Fetch movies and store in a dictionary
cursor.execute("UPDATE ongoing_series SET watched_duration = 1000")
conn.commit()