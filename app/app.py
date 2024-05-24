from flask import Flask, request, jsonify
import joblib
from werkzeug.utils import secure_filename
from MockModel import MockModel

app = Flask(__name__)

@app.route('/predictionB', methods=['POST'])
def predictFromFile():
    # Check if a file was sent
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400

    file = request.files['file']

    # If the user does not select a file, the browser might
    # submit an empty file part without a filename.
    if file.filename == '':
        return jsonify(error="No selected file"), 400

    # Read the file content
    data = file.read().decode('utf-8').splitlines()

    predictions = []
    
    model = joblib.load("models/model.pkl")

    for record in data:
        # Split the record by comma and convert each item to float
        record = list(float(x) for x in record.strip("'").replace(" ", "").split(","))
        print(record)
        predictions.append(model.predict(record))

    # Return the predictions in the response
    return jsonify(predictions=predictions)

if __name__ == '__main__':
    app.run(port=8080, debug=True)