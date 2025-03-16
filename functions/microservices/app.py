from flask import Flask, request, jsonify
from main.main import campaign_optimization
import sys

app = Flask(__name__)


@app.route('/', methods=['GET'])
def up():
    return 'READY', 200


@app.route('/distribution', methods=['POST'])
def compute_distribution():
    data = request.json
    test_names = data['...']
    number_of_node = data['...']

    if number_of_node < 0:
        return 'number of ... should be a positive value!'

    if number_of_node == 0:
        return 'number of ... should be bigger than zero!'

    if len(test_names) == 0:
        return 'there is not any ... to define distribute'

    # execute algorithm as a function
    distribution = campaign_optimization(test_names, number_of_node)
    # return json file of result contain tests names and node number
    return jsonify(distribution), 200


if __name__ == '__main__':
    app.run(host=app.config.get("HOST", "0.0.0.0"), port=app.config.get("PORT", 5000), debug=True)
