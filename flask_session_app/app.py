from flask import Flask, request, jsonify, session
from datetime import timedelta
import random

app = Flask(__name__)
app.secret_key = "super-secret-enterprise-key"
app.permanent_session_lifetime = timedelta(minutes=30)

# In-memory user store (enterprise apps use DB)
USERS = {}

def login_required():
    return "user" in session

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in USERS:
        return jsonify({"error": "User already exists"}), 400

    USERS[username] = password
    return jsonify({"message": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if USERS.get(username) != password:
        return jsonify({"error": "Invalid credentials"}), 401

    # ✅ Generate random number
    random_number = random.randint(100000, 999999)

    session.permanent = True
    session["user"] = username
    session["request_key"] = random_number

    return jsonify({
        "message": "Login successful, session created",
        "request_key": random_number
    }), 200


@app.route("/post", methods=["POST"])
def create_post():
    if not login_required():
        return jsonify({"error": "Unauthorized, no session"}), 401

    data = request.json
    client_key = data.get("request_key")

    # ✅ Validate random number
    if client_key != session.get("request_key"):
        return jsonify({"error": "Invalid request key"}), 403

    return jsonify({
        "message": "Post created successfully",
        "created_by": session["user"],
        "content": data.get("content")
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
