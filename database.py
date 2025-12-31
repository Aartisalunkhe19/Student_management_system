import sqlite3

def get_connection():
    return sqlite3.connect("students.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
    """)

    conn.commit()
    conn.close()
