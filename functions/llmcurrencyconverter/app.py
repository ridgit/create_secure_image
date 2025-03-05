from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from', default='USD', type=str)
    to_currency = request.args.get('to', default='EUR', type=str)
    amount = request.args.get('amount', default=1.0, type=float)

    response = requests.get('https://v6.exchangerate-api.com/v6/80f6cd0be8395230b0f5b1fe/latest/' + from_currency)
    data = response.json()

    rate = data['rates'][to_currency]
    converted_amount = amount * rate

    return {'converted_amount': converted_amount}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
