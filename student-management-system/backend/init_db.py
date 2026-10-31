import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("sms.db")
cursor = conn.cursor()

# --- Create students table ---
# --- Create students table ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
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
# --- Create attendance table ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
""")

# --- Create courses table ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    teacher_id INTEGER,
    FOREIGN KEY(teacher_id) REFERENCES teachers(id)
)
""")

# --- Create enrollment table ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
)
""")

# --- Create grades table ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    course_id INTEGER NOT NULL,
    grade TEXT NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
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
    # Insert sample attendance (only if table is empty)
cursor.execute("SELECT COUNT(*) FROM attendance")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)
    """, [
        ('ST001', '2026-10-20', 'Present'),
        ('ST002', '2026-10-20', 'Absent'),
        ('ST003', '2026-10-20', 'Present')
    ])

# Insert sample grades (only if table is empty)
cursor.execute("SELECT COUNT(*) FROM grades")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)
    """, [
        ('ST001', 1, 'A'),
        ('ST002', 1, 'B'),
        ('ST003', 2, 'C')
    ])

conn.commit()
conn.close()
print("Database initialized with students and admin account.")
