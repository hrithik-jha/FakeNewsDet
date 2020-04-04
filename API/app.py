from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import pandas as pd
import numpy as np
# Import the updated pickle reader

#Listening for requests
app = Flask(__name__)
@app.route('/')
def hello():
    return "Sup"

@app.route('/url', methods=["POST"])
def art_id():
    if 'url' in request.args:
        url = request.args.get('url')
    else:
        return "Error: No Id field provided."
    # TO-DO:
    # Insert pickle model reference
    # 
    return jsonify({'prediction': l})

app.run(debug=True)
