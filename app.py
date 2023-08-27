from lib.data import * # Import data.py
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify

# Create a Flask app
app = Flask(__name__)

# empty page with hello world

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run flask app
if __name__ == "__main__":
    app.run(debug=True)
    