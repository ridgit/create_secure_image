#!flask/bin/python
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Hello world endpoint
@app.route('/')
def hello():
    return 'Hello world!'

# Verify the status of the microservice
@app.route('/health')
def health():
    return '{ "status" : "UP" }'

# Get environment details
@app.route('/environment')
def environment():
    environment_data = {
        'platformUrl': os.getenv('C8Y_BASEURL'),
        'mqttPlatformUrl': os.getenv('C8Y_BASEURL_MQTT'),
        'tenant': os.getenv('C8Y_BOOTSTRAP_TENANT'),
        'user': os.getenv('C8Y_BOOTSTRAP_USER'),
        'password': os.getenv('C8Y_BOOTSTRAP_PASSWORD'),
        'microserviceIsolation': os.getenv('C8Y_MICROSERVICE_ISOLATION')
    }
    return jsonify(environment_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
