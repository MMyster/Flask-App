import pandas as pd
from flask import Flask, request, render_template, make_response

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/other')
def other():
    some_text = "Example"
    return render_template('other.html', text=some_text)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('select_letters')
def select_letters(s):
    return s[1::2]

if __name__ ==  '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)