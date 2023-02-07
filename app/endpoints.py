from flask import render_template
import os
from app import app


path = os.getcwd()

@app.route('/')
def index():
    logo = os.path.join(path, 'app', 'static', 'logo.png')
    return render_template('index.html')

@app.route('/blog')
def blog():
    return {"msg": "This is blog"}