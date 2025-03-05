#Cette application flask crée un point d'entrée HTTP POST où vous pouvez envoyer une requête JSON avec un champ "text". Elle vous renverra un JSON avec le nombre de mots dans le texte.
from flask import Flask, request
app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.get_json()['text']
    word_count = len(text.split())
    return {"word_count": word_count}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
