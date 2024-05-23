from flask import Flask, request, jsonify
import joblib
from MockModel import MockModel

# Załaduj model klasyfikatora binarnego
model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/predictionA', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(list(float(x) for x in data.values()))
    return jsonify(prediction=prediction)

if __name__ == '__main__':
    app.run(port=8080)