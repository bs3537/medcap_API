#https://www.kdnuggets.com/2019/01/build-api-machine-learning-model-using-flask.html

from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle 
import joblib
import json
import numpy as np
import gzip
from urllib.request import urlopen
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/')
    def index():
        return "Cannabis Strain Selector API"


    @app.route('/api/', methods=['GET'])
    def prediction():
        data = request.get_json()
        prediction = np.array2string(model.predict(data))

        return jsonify(prediction)
    return app

if __name__ == '__main__':
    fp=gzip.open('baseline_model_gzip.gz','rb')
    s= fp.read()
    model = joblib.load(s)
    app.run(debug=True)
