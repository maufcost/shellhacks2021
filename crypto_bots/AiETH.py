# TODO(developer): Uncomment and set the following variables
project_id = 'shellcoin'
compute_region = 'us-central1'
model_display_name = 'ethdailypricescol_20210925113152'
from google.cloud import automl_v1beta1 as automl

API_KEY = "redacted"

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

val = setup_before_prediction()
print("Price Prediction for ETH tmr: {}".format(val))
