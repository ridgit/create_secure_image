from flask import Flask, jsonify
import uuid

app = Flask(__name__)

@app.route('/')
def generate_uuid():
    return jsonify({"uuid": str(uuid.uuid4())})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
