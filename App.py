import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Fernando Dela Riva - 3rd Year BSIT - System Integration and Architecture - Semi Final Exam</h1>'

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
