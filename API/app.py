from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import pandas as pd
import numpy as np

#Listening for requests
app = Flask(__name__)
@app.route('/')
def hello():
    return "Server is listening..."

@app.route('/url', methods=["GET"])
def art_id():
    if 'url' in request.args:
        url = request.args.get('url')
    else:
        return "Error: No URL field provided."
    
    return jsonify({'prediction': "Functionality not added yet"})

app.run(debug=True)
