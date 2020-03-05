#https://www.kdnuggets.com/2019/01/build-api-machine-learning-model-using-flask.html

from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle 
import joblib
import json
import numpy as np
from urllib.request import urlopen
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/')
    def index():
        return "Cannabis Strain Selector API"


    @app.route('/api/', methods=['POST', 'GET'])
    def prediction():
        data = request.get_json()
        model = joblib.load(urlopen("https://storage.cloud.google.com/medcabapi/baseline_model2.pkl"))
        prediction = np.array2string(model.predict(data))

        return jsonify(prediction)
    return app

if __name__ == '__main__':
    model = joblib.load(urlopen("https://storage.cloud.google.com/medcabapi/baseline_model2.pkl"))
    app.run(debug=True)
