import time
from twilio.rest import Client
from trycourier import Courier
import string
import random
import json
import requests
import datetime
import math
from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS, cross_origin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
API_KEY = "579502ad14da14d6e8a443f88768712c2cf19363cd3e50995ec76353dc8fd5a6"
cred = credentials.Certificate('autosmscred.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def formatNumber(num):
	s = ""
	for i in str(num):
		if i.isnumeric():
			s+=i

	return "+1" + s[-9:] # currently just working w american numbers

def sendMessage(m, number, courier=True): # default send message to phone number
	if courier:
		client = Courier(auth_token="dk_prod_XAD3QDVD0SM6Q9NF9V0QPAAZG7NC")

		resp = client.send(
		  event="1T1VSAXN4H4ESTH3ESR0F3H6EB53",
		  recipient="Google_115516971900029641694", # Using Adam's message ID currently. I can add others later
		  profile={
		  },
		  data={
		    "first_name": "Adam",
		    "message": f"{m}"
		  },
		)

	else: # twilio
		account_sid = 'ACceb4154cae28ed11f11c1a90e560bab0'
		auth_token = 'c0109d61f19d3954f917342ab8d8b7a6'
		client = Client(account_sid, auth_token)

		message = client.mesages.create(
				body = m,
				from_='+18632926544',
				to=formatNumber(number)
			)


def convertSecs(seconds, granularity=1):
	intervals = (
	('weeks', 604800),  # 60 * 60 * 24 * 7
	('days', 86400),    # 60 * 60 * 24
	('hours', 3600),    # 60 * 60
	('minutes', 60),
	('seconds', 1),
				)
	result = []

	for name, count in intervals:
		value = seconds // count
		if value:
			seconds -= value * count
			if value == 1:
				name = name.rstrip('s')
			result.append("{} {}".format(value, name))
	return ', '.join(result[:granularity])

def portfolioAlert(coin, value, delta, number, threshold = .05): # delta is decimal. time in seconds
    m = ""
    if abs(delta) >= threshold:
        if delta < 0:
            m = f"📉 {coin} is down {delta*100:.2f}% since the last update! {value}📉"
        else:
            m = f"📈 {coin} is up {delta*100:.2f}% since the last update! {value}📈"
        sendMessage(m, number)

# Send this regardless:::
def portfolioAlertNothres(coin, value, delta, number):
    m = ""
    if delta < 0:
        m = f"📉 {coin} is down {delta*100:.2f}% since the last update! {value}📉"
    else:
        m = f"📈 {coin} is up {delta*100:.2f}% since the last update! {value}📈"
    sendMessage(m, number)


def update_coin_price(coin, number, value):
    # Add the current bitcoin price to the prices collection
    doc_ref = db.collection('prices').document(coin + number)
    doc_ref.set({
        u'price': value,
        u'coin': coin,
        u'phone': number
    })

# Every 10-mins check if the price change was significant
# If price changed more than 5%, we send
def send_sms_messages():
    prices = db.collection(u'prices').stream()
    for price in prices:
        le_copy = price.to_dict()
        current_price = query_for_current_price(le_copy['coin'])
        percentage_change = (current_price -  le_copy['price'])/le_copy['price']
        portfolioAlert(le_copy['coin'], current_price, percentage_change, le_copy['phone'])
        update_coin_price(le_copy['coin'], le_copy['phone'], current_price)

# Every 20min update
def send_periodic_message():
    prices = db.collection(u'prices').stream()
    for price in prices:
        le_copy = price.to_dict()
        current_price = query_for_current_price(le_copy['coin'])
        percentage_change = (current_price -  le_copy['price'])/le_copy['price']
        portfolioAlertNothres(le_copy['coin'], current_price, percentage_change, le_copy['phone'])
        update_coin_price(le_copy['coin'], le_copy['phone'], current_price)


def query_for_current_price(coin):
    url = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD&api_key={}".format(coin, API_KEY)
    response = requests.request("GET", url)
    return response.json().get("USD")

def technical_indicators_for_coin(coin):
    url = "https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest?fsym={}&api_key={}".format(coin, API_KEY)
    response = requests.request("GET", url)
    return response.json()

def process_technical_indicators(data):
    results = {"bearish":0, "bullish":0, "neutral":0}
    if data and data.get("Data"):
        results[data.get("Data").get("inOutVar").get("sentiment")] += 1
        results[data.get("Data").get("largetxsVar").get("sentiment")] += 1
        results[data.get("Data").get("addressesNetGrowth").get("sentiment")] += 1
        results[data.get("Data").get("concentrationVar").get("sentiment")] += 1
    return results

def get_indicators(coin):
    data = technical_indicators_for_coin(coin)
    res = process_technical_indicators(data)
    return res

def populate_db():
    doc_ref = db.collection('prices').document("ETH" + "9544786940")
    doc_ref.set({
        u'price': 2700,
        u'coin': "ETH",
        u'phone': "9544786940"
    })

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/sendsmstoall', methods=['GET'])
@cross_origin()
def sendsmstoall():
    send_periodic_message()
    return jsonify({'status':'OK'})

@app.route('/pricetrack', methods=['GET'])
@cross_origin()
def pricetrack():
    send_sms_messages()
    return jsonify({'status':'OK'})

#Return technical indicators
@app.route('/subscribe_user', methods=['POST'])
@cross_origin()
def subscribe():
    coin = request.form.get('coin')
    phone = request.form.get('phone')
    value = query_for_current_price(coin)
    update_coin_price(coin, phone, value)
    return jsonify({'status':'OK'})


# Start Flask backend
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
