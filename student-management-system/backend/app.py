
from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_admin_by_email, get_teacher_by_email
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

if __name__ == "__main__":
    app.run(debug=True)