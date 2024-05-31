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

    
    modelRF = joblib.load("../models/trained/rf_selected_model.joblib")
    modelXGB = joblib.load("../models/trained/xgb_selected_model.joblib")
    

    feature_names = data[0].strip("'").replace(" ", "").split(",")

    log_file_A = 'logs/modelRF.log'
    log_file_B = 'logs/modelXGB.log'

    # Create log files if they don't exist
    if not os.path.exists(log_file_A):
        os.makedirs(os.path.dirname(log_file_A), exist_ok=True)
        open(log_file_A, 'w').close()

    if not os.path.exists(log_file_B):
        os.makedirs(os.path.dirname(log_file_B), exist_ok=True)
        open(log_file_B, 'w').close()


    formatter = logging.Formatter('%(message)s')
    
    # Set up logging
    loggerRF = logging.getLogger('modelRF')
    handlerRF = logging.FileHandler('logs/modelRF.log')
    handlerRF.setFormatter(formatter)
    loggerRF.addHandler(handlerRF)
    loggerRF.setLevel(logging.INFO)

    loggerXGB = logging.getLogger('modelXGB')
    handlerXGB = logging.FileHandler('logs/modelXGB.log')
    handlerXGB.setFormatter(formatter)
    loggerXGB.addHandler(handlerXGB)
    loggerXGB.setLevel(logging.INFO)


    models = [modelRF, modelXGB] #more models can be added here
    loggers = [loggerRF, loggerXGB] #more loggers should be added here one for each model

    predictions = []


    # for record in data[1:20]:
    for record in data[1:]:
        # Split the record by comma and convert each item to float
        record = np.array([float(x) for x in record.strip("'").replace(" ", "").split(",")]).reshape(1,-1)
        record_df = pd.DataFrame(record, columns=feature_names).drop(columns=['user_id'])
        #extract user id and convert to int
        user_id = int(pd.DataFrame(record, columns=feature_names).user_id[0])

        # Randomly select a model
        modelIndex = random.choice([0, len(models)-1])
        model = models[modelIndex]
        logger = loggers[modelIndex]

        prediction = model.predict(record_df)
        prediction = bool(prediction)
        
        logLine = f"{user_id}, {prediction}"

        # Append the prediction to the predictions list
        predictions.append(prediction)

        # Log the prediction
        logger.info(logLine)

    # Return the predictions in the response
    return jsonify(predictions=predictions)

if __name__ == '__main__':
    app.run(port=8080, debug=True)