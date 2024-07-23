from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/hello', methods=['GET','POST'])
def hello():
    if request.method == 'GET' :
        return "GET Request  - Hello World\\n"
    elif request.method == 'POST' :
        return "POST Request - Hello World\n"

@app.route('/hello/<name>')
def greet(name):
    response = make_response(f"Hello {name}")
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream' # or text/plain
    return response

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1}+{number2} = {number1 + number2}"

@app.route('/handle_url_params')
def handle_url_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting} {name}'
    else: 
        return 'Some parameters are missing'
if __name__ ==  '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)