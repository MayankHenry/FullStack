from flask import Flask, render_template, redirect, request, url_for, jsonify, send_file
from models.student_model import fetch_db

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/student')
def students():
    student_data = fetch_db()
    return jsonify(student_data)

@app.route('/flask')
def index():
    return "Welcome to flask"

@app.route('/html')
def html():
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)