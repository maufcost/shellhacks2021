import time
import string
import random
import json
import requests
from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS, cross_origin


def get_unix_time(days=0, hours=0, minutes=0, seconds=0):
    return int(time.time())

# Creates a random string with letters and numbers with default length of 8.
def randomStringDigits(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/superapi', methods=['POST'])
@cross_origin()
def superapi():
    current_price = {}
    try:
        current_price = {"ETH": 2900}
    except Exception as e:
        current_location = {"ETH": 2900}

    return jsonify({'data': current_price})

@app.route('/test', methods=['POST'])
@cross_origin()
def test():
    return jsonify({'message': "OK"})

# Start Flask backend
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
