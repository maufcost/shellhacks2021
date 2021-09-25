import requests
import math

API_KEY = "redacted_for_now"

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

# Todo: Coinroute API
def query_for_current_price(coin):
    return 2900

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


print(start_bot_analysis("ETH", 5000))
#start_bot_analysis("ETH")

# 7 day low: 2677.64, high: 3541.73, diff: 864.09, % 32.27
# print(optimize_dip(32.27, 3400, 3541.73))
#
