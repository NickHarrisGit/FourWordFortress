from flask import Flask, render_template
from password_generator import generate_password
app = Flask(__name__)

@app.route('/')
def home():
    password = generate_password()
    return render_template('index.html', password=password)

