#Voici un exemple de code qui utilise l'API AlphaVantage pour obtenir des données d'actions :
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/stock/<string:ticker>', methods=['GET'])
def get_stock_data(ticker):
    API_KEY = 'RFSC3B5B5SP1YOWH'
    BASE_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={API_KEY}'
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        stock_data = response.json()["Time Series (Daily)"]
        return jsonify({'data': stock_data}), 200
    else:
        return jsonify({'message': 'Cannot get data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
