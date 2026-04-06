"""
Database config and connection management

Initialises the utilities for the app.
"""
import sqlite3

def get_connection():
    return sqlite3.connect("tickets.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()