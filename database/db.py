import sqlite3

def init_db():
    conn = sqlite3.connect("progress.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transcript TEXT,
            score REAL
        )
    """)

    conn.commit()
    conn.close()


def save_session(transcript, score):
    conn = sqlite3.connect("progress.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO sessions (transcript, score) VALUES (?, ?)",
        (transcript, score)
    )

    conn.commit()
    conn.close()