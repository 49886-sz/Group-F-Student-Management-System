import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("sms.db")
cursor = conn.cursor()

# --- Create students table ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

# Insert sample students (only if table is empty)
cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO students (id, name, class, status) VALUES (?, ?, ?, ?)
    """, [
        ('ST001', 'Ahmad Khan', 'Grade 10', 'Active'),
        ('ST002', 'Sara Ali', 'Grade 11', 'Active'),
        ('ST003', 'Mohammad Rahimi', 'Grade 9', 'Inactive'),
        ('ST004', 'Fatima Noor', 'Grade 12', 'Active')
    ])

# --- Create admins table ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")

# --- Create teachers table ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")
# Insert sample admin (only if not already exists)
cursor.execute("SELECT * FROM admins WHERE email = ?", ("admin@example.com",))
if cursor.fetchone() is None:
    cursor.execute("INSERT INTO admins (email, password_hash) VALUES (?, ?)", (
        "admin@example.com",
        generate_password_hash("admin123")  # password is 'admin123'
    ))


# Insert sample teacher (only if not already exists)
cursor.execute(
    "SELECT * FROM teachers WHERE email = ?",
    ("teacher@example.com",)
)

if cursor.fetchone() is None:
    cursor.execute(
        "INSERT INTO teachers (email, password_hash) VALUES (?, ?)",
        (
            "teacher@example.com",
            generate_password_hash("teacher123")
        )
    )
conn.commit()
conn.close()
print("Database initialized with students and admin account.")
