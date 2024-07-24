from fastapi import FastAPI, Query
import sqlite3
from pydantic import BaseModel
from typing import List

app = FastAPI()

class MemoryRecord(BaseModel):
    timestamp: int
    total: int
    free: int
    used: int

def get_memory_data(n: int):
    conn = sqlite3.connect('memory_data.db')
    c = conn.cursor()
    c.execute('''
        SELECT timestamp, total, free, used FROM memory ORDER BY id DESC LIMIT ?
    ''', (n,))
    rows = c.fetchall()
    conn.close()
    return [MemoryRecord(timestamp=row[0], total=row[1], free=row[2], used=row[3]) for row in rows]

@app.get('/memory')
def read_memory_data(limit: int = Query(10, description="Number of recent records to retrieve")):
    return get_memory_data(limit)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
