"""
Database config and connection management

Initialises the utilities for the app.
"""
import sqlite3
import os
DB_PATH = os.getenv("DB_PATH", "data/app.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    #Ticket stable
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        status TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Notes table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        ticket_id INTEGER NOT NULL,
        content TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()
