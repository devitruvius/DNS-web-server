from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_data():
    data = request.form['data']
    return f'Os dados enviados foram: {data}'

@app.route('/receive', methods=['GET'])
def receive_data():
    data = request.args.get('data')
    return f'Os dados enviados via GET são: {data}'

# Nova rota para soma usando GET
@app.route('/sum', methods=['GET'])
def sum_get():
    num1 = request.args.get('num1', type=int)
    num2 = request.args.get('num2', type=int)
    if num1 is not None and num2 is not None:
        result = num1 + num2
        return f'A soma de {num1} e {num2} é {result}'
    else:
        return 'Por favor, forneça dois números.', 400

# Nova rota para soma usando POST
@app.route('/sum', methods=['POST'])
def sum_post():
    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return f'A soma de {num1} e {num2} é {result}'
    except (ValueError, KeyError):
        return 'Por favor, forneça dois números válidos.', 400

if __name__ == '__main__':
    app.run()