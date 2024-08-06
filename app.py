import pandas as pd
from flask import Flask, request, render_template, make_response

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ ==  '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)