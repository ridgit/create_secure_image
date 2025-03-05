from flask import Flask, request

app = Flask(__name__)

responses = {
    "hello": "Hello, how can I help you?",
    "bye": "Goodbye, have a nice day!",
    # Vous pouvez ajouter autant de réponses que vous le souhaitez ici
}

@app.route('/', methods=['POST'])
def handle_message():
    message = request.form['message']
    response = responses.get(message, "Sorry, I didn't understand that.")
    return response, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
