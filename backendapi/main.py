import time
import string
import random
import json
import requests
import datetime
import math
from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS, cross_origin
from google.cloud import automl_v1beta1 as automl

project_id = 'shellcoin'
compute_region = 'us-central1'
model_display_name = 'ethdailypricescol_20210925113152'

class Client(object):

    token = "6c634e1eacecc4801b000249287fbf923d5c8824" # coinroutes portal API token

    url = 'https://staging.coinroutes.com/api/cost_calculator/'

    def __init__(self):

        self.session = requests.Session()
        self.session.headers = self.get_headers()
        print(self.session.headers)

    def get_headers(self):
        return {'Authorization': 'Token {}'.format(self.token)}


    def run(self, coin):
       req = {
        "currency_pair": "{}-USD".format(coin),  # currency pair to get prices for
        "exchanges": ["gdax", "gemini", "bitstamp"],  # exchanges to include in the cost calculation
        "side": "bids",  # "asks" is for the buy price, "bids" is for the sell price
        "quantity": 1,  # quantity of the target currency to get the price for
        "levels": 1000,  # number of price levels to consider.  Defaults to 1000 which is sufficient for most use cases

        # This is the name of the strategy to use for calculating available balances
        # Must be specified if use_balances = True.
        #  Strategies can be found at https://portal.coinroutes.com/api/strategies/
        "strategy": None,
        # Should available Balances be used to calculate the effective price?
        #  This will limit exchange selection to exchanges with balances on the specified strategy
        "use_balances": False,
        #'order_type': 'ioc',
        'use_funding_currency': False

        }

       bids_response =  requests.post(self.url, json=req, headers=self.get_headers())
       bids_data = bids_response.json()
       return bids_data.get("best_total_price")

API_KEY = "579502ad14da14d6e8a443f88768712c2cf19363cd3e50995ec76353dc8fd5a6"

def get_last_7_days(coin):
    url = "https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym=USD&limit=7&api_key={}".format(coin, API_KEY)
    response = requests.request("GET", url)
    return response.json()

def analyze_potential_max_peak(data):
    bot_max_peak =  -1

    if data and data.get("Data"):
        for each_day in data.get("Data").get("Data"):
            bot_max_peak = max(bot_max_peak, each_day.get('high'))

    return bot_max_peak

def analyze_potential_dip_peak(data):
    bot_dip_peak =  999_999_999

    if data and data.get("Data"):
        for each_day in data.get("Data").get("Data"):
            bot_dip_peak = min(bot_dip_peak, each_day.get('low'))

    return bot_dip_peak

def optimize_dip(percentage_change, dip_peak, max_peak):
    magic_constant = round(percentage_change/math.pi,2) #30 -> ~10 # 10 -> ~3
    regulated_percentage_change = percentage_change - 2 * magic_constant/(math.pi/3)

    maximum_percentage_change_abs = min(10, max(percentage_change * 3, 5))
    capped_percentage_change_distribution = max(maximum_percentage_change_abs, regulated_percentage_change)

    redistributed_low_range = dip_peak - dip_peak*( ( 0.05 + capped_percentage_change_distribution/100)/(math.pi/2))
    redistributed_high_range = max_peak + max_peak * ( 0.05 + (capped_percentage_change_distribution/100)/(math.pi/2))

    return [round(redistributed_low_range, 2), round(redistributed_high_range,2)]

def generate_sample_transactions(coin, investment, divisions, low, high, current_price):
    step = (high-low)/divisions
    # Allocate 50% for current price
    first_allocation = {'buy':current_price, 'sell':round(max(high - high*0.05, current_price * 1.10),2), 'coin':coin, 'investment':round(investment * 0.5, 2)}
    investment -= investment * 0.5
    # [{buy:current_price, sell:high, coin:coin, investment}]
    transactions = [first_allocation]
    for i in range(divisions):
        buy_price = low
        sell_price = low + step
        amt = round(investment/divisions, 2)
        investment -= amt
        low = low + step
        transaction = {'buy':round(buy_price,2), 'sell':round(sell_price,2), 'coin':coin, 'investment':amt}
        transactions.append(transaction)
    return transactions

def start_bot_analysis(coin, investment):

    last_seven_days_data = get_last_7_days(coin)
    dip_peak = analyze_potential_dip_peak(last_seven_days_data)
    max_peak = analyze_potential_max_peak(last_seven_days_data)

    difference = round(max_peak - dip_peak, 2)
    percentage_change = round(difference/dip_peak * 100, 2)

    print("7 day low: {}, high: {}, diff: {}, % {}".format(dip_peak, max_peak, difference, percentage_change))
    bot_low, bot_high = optimize_dip(percentage_change, dip_peak, max_peak)
    new_percentage_change =  (bot_high-bot_low)/bot_low * 100

    # capped at 100 divisions
    # If percentage change is like 30% -> We want like 30-60 divisions (each division will have at least a profit of 0.66%)
    amt_of_divisions = min(100, int(new_percentage_change * 1.5))
    current_price = query_for_current_price(coin)
    transactions = generate_sample_transactions(coin, investment, amt_of_divisions, bot_low, bot_high, current_price)
    print("Based on our 7-day analysis, we've compiled this transaction list:")
    return transactions

def get_unix_time(days=0, hours=0, minutes=0, seconds=0):
    return int(time.time())

# Creates a random string with letters and numbers with default length of 8.
def randomStringDigits(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# TODO: Implement Back up method
def query_for_current_price(coin):
    url = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD&api_key={}".format(coin, API_KEY)
    response = requests.request("GET", url)
    return response.json().get("USD")

def get_price_of_coin(coin):
    try:
        c = Client()
        return c.run(coin)
    except Exception as e:
        return query_for_current_price(coin)

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

def make_ETH_prediction(inputs):
    client = automl.TablesClient(project=project_id, region=compute_region)
    response = client.predict(model_display_name=model_display_name, inputs=inputs)
    for result in response.payload:
        return result.tables.value

def generate_inputs():
    # This is how we would get thedata for the last 5 days
    #data = get_last_5_days("ETH")

    # For the sake of the hackathon & save API access will send this cached data
    # which is accurate and represents real values from 5 days ago
    cached = {'prevo1':2928.59,
              'prevh1':2965.48,
              'prevl1':2812.7,
              'prevv1':973830,
              'prevp2':2928.57,
              'prevo2':3152.92,
              'prevh2': 3158.38,
              'prevl2':2740.06,
              'prevv2':1740000,
              'prevp3':3152.92,
              'prevo3':3077.8,
              'prevh3':3173,
              "prevl3":3035.96,
              "prevv3":841540,
              "prevp4":3077.78,
              "prevo4":2764.71,
              "prevh4":3087.97,
              "prevl4":2740.58,
              "prevv4":1190000,
              "prevp5":2761.52,
              "prevo5":2976.7,
              "prevh5":3101.88,
              "prevl5":2659.71,
              "prevv5":1790000,
              "Date":"26-Sep-21"}
    return cached

# Get ETH data from the last 5 day
def get_last_5_days(coin):
    url = "https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym=USD&limit=5&api_key={}".format(coin, API_KEY)
    response = requests.request("GET", url)
    return response.json()

def setup_before_prediction():
    data = generate_inputs()
    val = make_ETH_prediction(data)
    return val


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/coinprice', methods=['POST'])
@cross_origin()
def coinprice():
    coin = request.form.get('coin')
    current_price = {}
    try:
        current_price = {coin: get_price_of_coin(coin)}
    except Exception as e:
        current_price = {coin: query_for_current_price(coin)}

    return jsonify(current_price)

@app.route('/oldprices', methods=['POST'])
@cross_origin()
def oldpricecoin():
    coin = request.form.get('coin')
    data = get_last_7_days(coin)
    return jsonify(data)

# DivideNConquer Bot
@app.route('/dncbot', methods=['POST'])
@cross_origin()
def DivideNConquerBotAPI():
    coin = request.form.get('coin')
    investment = request.form.get('investment')
    place_transactions = start_bot_analysis(coin, float(investment))
    return jsonify({'transactions': place_transactions})

# Return technical indicators
@app.route('/technical', methods=['POST'])
@cross_origin()
def technical_indicators():
    coin = request.form.get('coin')
    res = get_indicators(coin)
    return jsonify(res)

@app.route('/ethprediction', methods=['POST'])
@cross_origin()
def predicteth():
    predicted_val = round(setup_before_prediction().number_value, 2)
    return jsonify({'value':predicted_val})

# Start Flask backend
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
