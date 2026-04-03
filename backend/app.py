from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('../models/best_model.pkl', 'rb'))
vectorizer = pickle.load(open('../models/vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return "Spam Classifier API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get('message')

    vec = vectorizer.transform([message])
    pred = model.predict(vec)[0]

    result = 'Spam' if pred == 1 else 'Ham'

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
