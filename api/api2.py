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


    @app.route('/api/', methods=['POST'])
    def prediction():
        data = request.get_json()
        prediction = np.array2string(model.predict(data))

        return jsonify(prediction)
    return app

if __name__ == '__main__':
    model = joblib.load(urlopen("https://drive.google.com/file/d/1CIpEtDRgr3cicKeU_qyKMS_mMPS-EBOq/view?usp=sharing"))
    app.run(debug=True)
