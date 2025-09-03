# history.py

import sqlite3
from datetime import datetime

DB_NAME = "moodify_history.db"


# ✅ Initialize Database
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    emotion TEXT,
                    title TEXT,
                    link TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()


# ✅ Add new record
def add_record(emotion, title, link):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO history (emotion, title, link, timestamp) VALUES (?, ?, ?, ?)",
              (emotion, title, link, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()


# ✅ Fetch all records
def fetch_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT emotion, title, link, timestamp FROM history ORDER BY id DESC LIMIT 20")
    rows = c.fetchall()
    conn.close()
    return rows


# ✅ Clear all history
def clear_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM history")
    conn.commit()
    conn.close()
