#!/anaconda3/bin/python3
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'200',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'a911424d-c36a-43be-8bb4-5116acdf49f3',
}

session = Session()
session.headers.update(headers)
try:
  response = session.get(url, params=parameters)
  # print(response.text)
  data = json.loads(response.text)

  crypto_data={}

  # with open("cripto_currenci.xml", "w") as f: # шапка xml
  #   f.write('<ValCurs Date="%s" name="Crypto Currency Coinmarketcap">' % data['status']['timestamp'])
  #
  for i in data['data']:
  #
  #   with open("cripto_currenci.xml", "a") as f: # Записываем все данные о вылютах
  #     f.write('<Valute ID="%d"><Name>%s</Name><Value>%s</Value></Valute>' % (i['id'], i['symbol'], str(i['quote']['USD']['price']).replace(".", ",")))
  #
    crypto_data[i["symbol"]] = i["quote"]["USD"]["price"]
  #
  # with open("cripto_currenci.xml", "a") as f: # футер xml
  #   f.write('</ValCurs>')

  my_portfolio = ["XEM", "BTS", "XRP", "XMR", "DGB", "EOS", "SC", "ZEC", "ARDR", "LTC"]

  for i in my_portfolio:
    # print(i)
    # print(crypto_data[i])
    print(str(crypto_data[i]).replace(".", ","))

  # for i in crypto_data:
  #   print(i, " ", crypto_data[i])
  # for i in crypto_data:
  #   print(str(crypto_data[i]).replace(".", ","))
  # print(response.text)
  # except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
