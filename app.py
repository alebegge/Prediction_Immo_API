import json
from datetime import datetime
from flask import Flask, request, jsonify, abort
from predict.prediction import predict
from preprocessing.cleaning_data import preprocess

app = Flask(__name__)

@app.route('/', methods=["GET"])
def alive():
    return f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - This server is alive."

@app.route('/predict', methods=["GET", "POST"])
def predicted():
    error = None
    input_json = request.get_json(force=True)
    if request.method == 'POST':
        input_json = preprocess(input_json)
        if input_json:
            return predict(input_json)
        else:
            error = 'Invalid data, please refer to the documentation.'
            return error
    else:
        error = 'This route only takes POST as method for now.'
        return error

if __name__ == '__main__':
    app.run(port=5000, debug=True)