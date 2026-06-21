import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    issue TEXT,
    priority TEXT,
    status TEXT,
    escalated BOOLEAN,
    assigned_agent TEXT,
    created_at TEXT,
    updated_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ticket_comments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id INTEGER,
    comment TEXT,
    created_at TEXT,
    FOREIGN KEY(ticket_id) REFERENCES tickets(id)
)
""")

connection.commit()

# database.py

