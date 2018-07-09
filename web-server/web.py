from flask import Flask
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/bye')
def bye_func():
    return '''
    <!doctype html>
    <title>Bye</title>
    <h1>BYE</h1>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
