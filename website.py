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

if __name__ == '__main__':
    app.run(debug = True)
