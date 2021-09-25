import websockets
import aiohttp
import json
import asyncio
from decimal import Decimal
import aiohttp.web
import logging
import os


logging.basicConfig(level=logging.WARNING)

PAIRS = ['BTC-AUD', 'ETH-AUD', 'LTC-AUD', 'XRP-AUD', 'BCH-AUD', 'USDT-AUD', 'EOS-AUD', 'XLM-AUD', 'DOT-AUD', 'LINK-AUD', 'USDC-AUD', 'BSV-AUD', 'ADA-AUD', 'DOGE-AUD',

        'BTC-USD']


class PriceService(object):
    currency_pairs = {}

    # todo add support for ccys only listed in USDT / BTC: NEO, ENJ, EGLD, NEAR, AAVE
    prices = {}
    exchanges = ['gdax', 'gemini', 'kraken', 'bitstamp', 'b2c2', 'cumberland', 'hehmeyer', 'binance']
    http_port = 9000
    http_address='127.0.0.1'

    BASE_URL = "wss://portal.coinroutes.com/api/"
    SOR_TOKEN = "6c634e1eacecc4801b000249287fbf923d5c8824"
    FUNDING_CCY = "USD" # change this to your desired base

    @property
    def url(self):
        return "{}streaming/cbbo/?token={}".format(self.BASE_URL, self.SOR_TOKEN)

    def _best_side(self, side):
        side_data =  [i for i in side if i['exchange'] in self.exchanges]
        if len(side_data):
            return side_data[0]
        return None

    def _process_cbbo(self, message):
        currency, funding = message['product'].split('-')
        best_bid, best_ask = self._best_side(message['bids']), self._best_side(message['asks'])
        if best_bid and best_ask:
            price = self.currency_pairs[message['product']] =  str((Decimal(best_ask['price']) + Decimal(best_bid['price'])) / 2)
            if funding==self.FUNDING_CCY:
                self.prices[currency] = price


    async def _connect_currency(self, pair):
        print("connect {} {}".format(pair, self.url))
        while True:
            try:
                async with websockets.connect(self.url, timeout=30, max_queue=1000 ) as websocket:
                    query = {"currency_pair":pair,"size_filter":"0.00","sample":1}
                    print("ws connect {} {}".format(pair, self.url))
                    await websocket.send(json.dumps(query))
                    print(" {} data loop".format(pair))
                    while True:
                        message = json.loads(await websocket.recv())
                        if message.get('errors'):
                            print(message)
                            await asyncio.sleep(60)
                        else:
                            self._process_cbbo(message)
            except websockets.exceptions.InvalidStatusCode as e:
                if e.status_code == 403:
                    print("Rate limited {}, sleeping".format(pair))
                    await asyncio.sleep(60)
            except Exception as e:
                import traceback; traceback.print_exc()

    async def connect_data(self):
        futures = [ asyncio.ensure_future(self._connect_currency(pair)) for pair in PAIRS]
        await asyncio.wait(futures,return_when=asyncio.FIRST_COMPLETED)


    async def rest_prices(self, request):
        return aiohttp.web.json_response(self.prices)

    async def rest_pair_prices(self, request):
        return aiohttp.web.json_response(self.currency_pairs)

    async def http_server(self):
        self.http_app = aiohttp.web.Application()
        self.http_app.add_routes([
            aiohttp.web.get('/prices', self.rest_prices),
            aiohttp.web.get('/pair_prices', self.rest_pair_prices),

            ])

        self.http_runner = aiohttp.web.AppRunner(self.http_app)

        await self.http_runner.setup()
        try:
            self.http_site = aiohttp.web.TCPSite(self.http_runner,
                    self.http_address, self.http_port, reuse_address=True)
            await self.http_site.start()
            await self.connect_data()
        finally:
            await self.http_runner.cleanup()

    def main(self):
        asyncio.set_event_loop(asyncio.new_event_loop())

        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.http_server())

service = PriceService()
service.main()
