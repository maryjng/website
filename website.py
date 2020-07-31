from flask import Flask, url_for, render_template

app = FLASK(__name__)

#always do set FLASK_APP=website.py in command first

@app.route('/')
    def index():
