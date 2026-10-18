import sqlite3

conn = sqlite3.connect("sms.db")
cursor = conn.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

# Insert sample students
cursor.executemany("""
INSERT INTO students (id, name, class, status) VALUES (?, ?, ?, ?)
""", [
    ('ST001', 'Ahmad Khan', 'Grade 10', 'Active'),
    ('ST002', 'Sara Ali', 'Grade 11', 'Active'),
    ('ST003', 'Mohammad Rahimi', 'Grade 9', 'Inactive'),
    ('ST004', 'Fatima Noor', 'Grade 12', 'Active')
])

conn.commit()
conn.close()
