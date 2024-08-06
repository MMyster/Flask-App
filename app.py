from flask import Flask, request, render_template, make_response, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/other')
def other():
    some_text = "Example"
    return render_template('other.html', text=some_text)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET' :
        return render_template('login.html')
    if request.method == 'POST' :
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "mlatoundji" and password=="admin":
            return 'Success'
        else:
            return 'Failure'

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    if request.method == 'POST':
        return ""
    
@app.route('/request')
def request():
        return render_template('request.html')

    
@app.route('/handle_post', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()
        name = data['name']
        greetings = data['greetings']

        with open('file.txt', 'w') as file:
            file.write(f'Name: {name}, Greetings: {greetings}')

        return jsonify({'message': 'Successfully written!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('select_letters')
def select_letters(s):
    return s[1::2]

if __name__ ==  '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)