from flask import Flask, request, jsonify
import joblib
from werkzeug.utils import secure_filename
from MockModel import MockModel
import numpy as np

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
    
    model = joblib.load("models/rf_selected_model.joblib")

    for record in data[1:20]:
        # Split the record by comma and convert each item to float
        print(record)
        record = np.array([float(x) for x in record.strip("'").replace(" ", "").split(",")]).reshape(-1,1)
        print(record)
        predictions.append("True")

    # Return the predictions in the response
    return jsonify(predictions=predictions)

if __name__ == '__main__':
    app.run(port=8080, debug=True)