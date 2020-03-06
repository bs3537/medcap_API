from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle 
import joblib
import json
import numpy as np


app = Flask(__name__)


def create_app():

    @app.route('/')
    def index():
        return "Cannabis Strain Recommender for medical purpose"


    @app.route('/api/', methods=['POST'])
    def prediction():
        data = request.get_json()
        prediction = np.array2string(model.predict(data))

        return jsonify(prediction)

    return app

if __name__ == '__main__':
    model = joblib.load('potguide_model.pkl')
    app.run(debug=True)
