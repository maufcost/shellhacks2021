import datetime
import json
import requests
import os

class Client(object):

    token = "redacted"

    url = 'https://portal.coinroutes.com/api/cost_calculator/'

    def __init__(self):

        self.session = requests.Session()
        self.session.headers = self.get_headers()
        print(self.session.headers)

    def get_headers(self):
        return {'Authorization': 'Token {}'.format(self.token)}


    def run(self):
       req = {
        "currency_pair": "BTC-USD",  # currency pair to get prices for
        "exchanges": ["gdax","gemini","itbit","kraken","bitstamp"],  # exchanges to include in the cost calculation
        "side": "asks",  # "asks" is for the buy price, "bids" is for the sell price
        "quantity": 100,  # quantity of the target currency to get the price for
        "levels": 1000,  # number of price levels to consider.  Defaults to 1000 which is sufficient for most use cases

        # This is the name of the strategy to use for calculating available balances
        # Must be specified if use_balances = True.
        #  Strategies can be found at https://portal.coinroutes.com/api/strategies/
        "strategy": None,
        # Should available Balances be used to calculate the effective price?
        #  This will limit exchange selection to exchanges with balances on the specified strategy
        "use_balances": False,

        }

       # "asks" is to get the buy price
       req['side'] = "asks"
       asks_response =  self.session.post(self.url, data=req)
       print(asks_response.text)
       asks_data = asks_response.json()

       # "bids" is to get the sell price
       req['side'] = 'bids'
       bids_response =  self.session.post(self.url, data=req)
       bids_data = bids_response.json()

       buy_avg_price = asks_data.get('best_average_price')  # This is the effective price per coin without fees
       buy_first_price = asks_data.get('first_price') # this is the first price in the consolidated order book
       buy_cost = buy_avg_price - buy_first_price


       sell_avg_price = bids_data.get('best_average_price')
       sell_first_price = bids_data.get('first_price')
       sell_cost = sell_first_price - sell_avg_price

       print("Buy Cost: {} Sell Cost: {}".format(buy_cost, sell_cost))

c = Client()
c.run()
