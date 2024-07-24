import sqlite3
import time
import psutil
from datetime import datetime

def create_db():
    conn = sqlite3.connect('memory_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            total INTEGER,
            free INTEGER,
            used INTEGER
        )
    ''')
    conn.commit()
    conn.close()
