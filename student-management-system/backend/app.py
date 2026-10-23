from flask import Flask, request, jsonify
from flask_cors import CORS
from database import (
    get_admin_by_email,
    get_teacher_by_email,
    get_attendance,
    get_courses,
    get_enrollment,
    get_grades
)
from werkzeug.security import check_password_hash
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Welcome to the Student Management System!"

@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "Email and password are required"
        }), 400

    user = get_admin_by_email(email)
    role = "admin"

    if not user:
        user = get_teacher_by_email(email)
        role = "teacher"

    if user and check_password_hash(user["password_hash"], password):
        return jsonify({
            "success": True,
            "message": "Login successful",
            "role": role,
            "token": "mock-token"
        })

    return jsonify({
        "success": False,
        "message": "Invalid email or password"
    }), 401


@app.route("/api/students", methods=["GET"])
def get_students():
    conn = sqlite3.connect("sms.db")
    conn.row_factory = sqlite3.Row

    try:
        rows = conn.execute(
            "SELECT id, name, class, status FROM students"
        ).fetchall()
        return jsonify([dict(row) for row in rows])
    finally:
        conn.close()


# --- New routes ---
@app.route("/api/attendance", methods=["GET"])
def attendance():
    return jsonify(get_attendance())

@app.route("/api/courses", methods=["GET"])
def courses():
    return jsonify(get_courses())
@app.route("/api/courses", methods=["POST"])
def add_course():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    teacher_id = data.get("teacher_id")

    if not name:
        return jsonify({"success": False, "message": "Course name is required"}), 400

    conn = sqlite3.connect("sms.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO courses (name, description, teacher_id) VALUES (?, ?, ?)",
        (name, description, teacher_id)
    )
    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": "Course added successfully"}), 201


@app.route("/api/enrollment", methods=["GET"])
def enrollment():
    return jsonify(get_enrollment())

@app.route("/api/grades", methods=["GET"])
def grades():
    return jsonify(get_grades())


if __name__ == "__main__":
    app.run(debug=True)
