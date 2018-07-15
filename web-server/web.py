import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def homepage():
    title = "Epic Tutorials"
    try:
        return render_template("example_bootstrap.html")
    except Exception as e:
        return "Exception occur " + str(e)

@app.route('/hello')
def hello_world():
    return 'Hello World'

@app.route('/a')
def a_page():
    return render_template("a.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
