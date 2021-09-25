from twilio.rest import Client
from trycourier import Courier


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
		    first_name: "Adam",
		    message: f"{m}"
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

def portfolioAlert(coin, val, delta, time, number, threshold = .05): # delta is decimal. time in seconds
	m = ""
	if abs(delta) >= threshold:
		if delta < 0:
			m = f"📉 {coin} is down {delta*100:.2f}% is the last {convertSecs(time)} !📉"
		else:
			m = f"📈 {coin} is up {delta*100:.2f}% is the last {convertSecs(time)} !📈"

	sendMessage(m, number)

def bizSponsor(company, contribution, number):
	sendMessage(f"♥ {company} is having a ", number) # lol idk, we can work on this later
