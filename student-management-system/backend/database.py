import sqlite3

def get_admin_by_email(email):
    conn = sqlite3.connect("sms.db")
    conn.row_factory = sqlite3.Row

    try:
        row = conn.execute(
            "SELECT email, password_hash FROM admins WHERE email = ?",
            (email,)
        ).fetchone()

        if row:
            user_dict = dict(row)
            user_dict['role'] = 'admin'  # <-- Explicitly inject the role here
            return user_dict
        return None
    finally:
        conn.close()


def get_teacher_by_email(email):
    conn = sqlite3.connect("sms.db")
    conn.row_factory = sqlite3.Row

    try:
        row = conn.execute(
            "SELECT email, password_hash FROM teachers WHERE email = ?",
            (email,)
        ).fetchone()

        if row:
            user_dict = dict(row)
            user_dict['role'] = 'teacher'  # <-- Explicitly inject the role here
            return user_dict
        return None
    finally:
        conn.close()
