import requests
API_KEY = "redacted"

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

print("Technical Indicators for DOGE")
print(get_indicators("DOGE"))
