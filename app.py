
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

@app.route("/api/hello/<name>")
def hello_name(name):
    """
    Return a hello message with name
    """
    return jsonify({"hello": name})

@app.route("/api/whoami")
def whoami():
    """
    Return a JSON object with the name, ip, and user agent
    """
    return jsonify(
        name=request.remote_addr,
        ip=request.remote_addr,
        useragent=request.user_agent.string
    )

@app.route("/api/whoami/<name>")
def whoami_name(name):
    """
    Return a JSON object with the name, ip, and user agent
    """
    return jsonify(
        name=name,
        ip=request.remote_addr,
        useragent=request.user_agent.string
    )


import pandas as pd 
from keras.models import load_model

model = load_model('.\model')

@app.route('/classify', methods=['POST'])
def classify():

    data = request.get_json()
    pixels = pd.DataFrame(data['pixels']).T
    prediction = model.predict(pixels)
    prediction_list = prediction.tolist()

    return jsonify({'predict': prediction_list[0]})


##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()