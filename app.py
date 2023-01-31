
"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

import os
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify

##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

##########################################################################
## Routes
##########################################################################

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/hello")
def hello():
    """
    Return a hello message
    """
    return jsonify({"hello": "world"})

import numpy as np
import pandas as pd 
from keras.models import load_model

model = load_model('.\model')

@app.route('/classify', methods=['POST'])
def classify():

    data = request.get_json()
    print(data)

    pixels = pd.DataFrame(data['pixels']).T
    print(pixels)

    prediction = model.predict(pixels)
    print(prediction[0])

    prediction_list = prediction.tolist()

    return jsonify({'predict': prediction_list[0]})


##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()