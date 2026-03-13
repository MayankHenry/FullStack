from flask import Flask, app, render_template, redirect, request, url_for, jsonify, send_file
from models.student_model import fetch_db



app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/register', methods=["POST"])
def register():
    if request.method == "POST":
        data = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        if not data or not email or not password:
            return "Please fill all the fields"
        if len(password) < 6:
            return "Password must be at least 6 characters long"
        print(f"Received data: {data}, {email}, {password}")
    return render_template('register.html')

app.run()    