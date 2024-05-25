from flask import Flask, request, jsonify
import joblib
from werkzeug.utils import secure_filename
from MockModel import MockModel
import numpy as np
import pandas as pd
import random
import logging
import os


app = Flask(__name__)

@app.route('/prediction', methods=['POST'])
def predictFromFile():
    # Check if a file was sent
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400

    file = request.files['file']

    # If the user does not select a file, the browser might
    # submit an empty file part without a filename.
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    
    data = file.read().decode('utf-8').splitlines()

    predictions = []
    
    modelA = joblib.load("models/rf_selected_model.joblib")
    modelB = joblib.load("models/xgb_selected_model.joblib")
    

    feature_names = data[0].strip("'").replace(" ", "").split(",")

    log_file_A = 'logs/modelA.log'
    log_file_B = 'logs/modelB.log'

    # Create log files if they don't exist
    if not os.path.exists(log_file_A):
        os.makedirs(os.path.dirname(log_file_A), exist_ok=True)
        open(log_file_A, 'w').close()

    if not os.path.exists(log_file_B):
        os.makedirs(os.path.dirname(log_file_B), exist_ok=True)
        open(log_file_B, 'w').close()


    formatter = logging.Formatter('%(message)s')
    
    # Set up logging
    loggerA = logging.getLogger('ModelA')
    handlerA = logging.FileHandler('logs/modelA.log')
    handlerA.setFormatter(formatter)
    loggerA.addHandler(handlerA)
    loggerA.setLevel(logging.INFO)

    loggerB = logging.getLogger('ModelB')
    handlerB = logging.FileHandler('logs/modelB.log')
    handlerB.setFormatter(formatter)
    loggerB.addHandler(handlerB)
    loggerB.setLevel(logging.INFO)


    models = [modelA, modelB]
    loggers = [loggerA, loggerB]

    for record in data[1:20]:
        # Split the record by comma and convert each item to float
        record = np.array([float(x) for x in record.strip("'").replace(" ", "").split(",")]).reshape(1,-1)
        record_df = pd.DataFrame(record, columns=feature_names)

        # Randomly select a model
        index = random.choice([0, 1])
        model = models[index]
        logger = loggers[index]

        prediction = model.predict(record_df)

        # Append the prediction to the predictions list
        predictions.append(bool(prediction[0]))

        # Log the prediction
        logger.info(str(bool(prediction[0])))
    # Return the predictions in the response
    return jsonify(predictions=predictions)

if __name__ == '__main__':
    app.run(port=8080, debug=True)