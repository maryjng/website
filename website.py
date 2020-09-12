import flask
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

#always do set FLASK_APP=website.py in command first

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kitty/')
def kitty():
    return render_template('kitty.html')

@app.route('/aboutme/')
def aboutme():
    return render_template('aboutme.html')

@app.route('/photos/')
def photos():
    return render_template('photos.html')

@app.route('/art/')
def art():
    return render_template('art.html')

if __name__ == '__main__':
    app.run(debug=True)
