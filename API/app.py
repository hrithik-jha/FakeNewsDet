from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import pandas as pd
import numpy as np

#Listening for requests
app = Flask(__name__)
@app.route('/')
def hello():
    return "Sup"

@app.route('/url', methods=["POST"])
def movie_id():
    if 'url' in request.args:
        url = request.args.get('url')
    else:
        return "Error: No Id field provided."

    return jsonify({'recommendations': l})

app.run(debug=True)
