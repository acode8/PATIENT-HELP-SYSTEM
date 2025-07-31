import sqlite3
from datetime import datetime

def log_help_request(help_type):
    conn = sqlite3.connect('help_requests.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs 
                 (timestamp TEXT, help_type TEXT)''')
    c.execute("INSERT INTO logs VALUES (?, ?)", (datetime.now().isoformat(), help_type))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect('help_requests.db')
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY timestamp DESC")
    logs = c.fetchall()
    conn.close()
    return logs
