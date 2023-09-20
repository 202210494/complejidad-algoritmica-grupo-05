import sqlite3

conn = sqlite3.connect("social_media.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date_of_birth DATE,
        country TEXT,
        phone_number TEXT,
        joined_date DATE DEFAULT CURRENT_TIMESTAMP
    )
"""
)

conn.commit()
conn.close()
