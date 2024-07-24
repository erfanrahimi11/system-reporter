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

def log_memory_data():
    conn = sqlite3.connect('memory_data.db')
    c = conn.cursor()
    while True:
        memory_info = psutil.virtual_memory()
        timestamp = int(time.time())
        total = memory_info.total // 1024 // 1024
        free = memory_info.available // 1024 // 1024
        used = total - free
        c.execute('''
            INSERT INTO memory (timestamp, total, free, used) VALUES (?, ?, ?, ?)
        ''', (timestamp, total, free, used))
        conn.commit()
        time.sleep(60)  # wait for 1 minute

if __name__ == '__main__':
    create_db()
    log_memory_data()
