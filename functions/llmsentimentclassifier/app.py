from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
import joblib
import nltk

nltk.download('stopwords')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    vectorizer = TfidfVectorizer(stop_words = stopwords.words('english'))
    model = joblib.load('sentiment_model.joblib')
    text = data['text']
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return jsonify({'prediction': prediction.tolist()[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
