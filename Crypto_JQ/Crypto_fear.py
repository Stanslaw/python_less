from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



url_fear = 'https://api.alternative.me/fng/?limit=0'
url_btc = 'https://api.alternative.me/v2/ticker/?limit=20'
# parameters = {
#   'start':'1',
#   'limit':'200',
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': 'a911424d-c36a-43be-8bb4-5116acdf49f3',
# }

session_fear = Session()
session_btc = Session()
# session.headers.update(headers)

try:
  response_fear = session_fear.get(url_fear)
  # print(response.text)
  data_fear = json.loads(response_fear.text)

  response_btc = session_btc.get(url_btc)
  # print(response_btc.text)
  data_btc = json.loads(response_btc.text)

  print(data_btc['data'])

  # for i in data_fear['data']:
  #   print(i['timestamp']," ", i['value'])



  # for i in data['data']:
  #   crypto_data[i["symbol"]] = i["quote"]["USD"]["price"]


except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)





