from bs4 import BeautifulSoup
import requests
from datetime import datetime

def mondejar_weather():
    r = requests.get('https://www.wunderground.com/weather/es/mond%C3%A9jar/')
    soup = BeautifulSoup(r.text, 'lxml')

    tiempo = soup.find_all('span', class_='wu-value wu-value-to')
    texto_tiempo = int(tiempo[0].text)
    celsius = (texto_tiempo - 32) * 5/9
    redondeo = round(celsius)

    condiciones = soup.find_all('div', class_='condition-icon')
    condiciones_texto = condiciones[0].text

    output = ("Mondejar have now " + str(redondeo) +
              "ºC and have " + condiciones_texto)
    print(output)
    return output

def noticias():
    r = requests.get('https://www.elespanol.com/')
    soup = BeautifulSoup(r.text, 'lxml')
    news = soup.find_all('h2', class_="art__title")

    newslist = []
    for new in news:
        newslist.append(new)

    first = newslist[0]
    second = newslist[1]

    noticia1 = first.text
    noticia2 = second.text

    print(noticia1)
    print(noticia2)
    
    return noticia1 + noticia2

def noticias_economicas():
    r = requests.get('https://www.elespanol.com/invertia/')
    soup = BeautifulSoup(r.text, 'lxml')
    news = soup.find_all('h3', class_="head head--l")

    newslist = []
    for new in news:
        newslist.append(new)


    first = newslist[0]
    second = newslist[1]

    noticia1 = first.text
    noticia2 = second.text

    print(noticia1)
    print(noticia2)

    return noticia1 + noticia2

def apple_price():
      main_url = "https://finance.yahoo.com/quote/AAPL/"
      req = requests.get(main_url)
      soup = BeautifulSoup(req.text, "html.parser")
      ApplePrice = soup.find("fin-streamer", class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)")
      output = "Apple Inc.(APPL) today: $" + ApplePrice.text
      print(output)
      return output

def tesla_price():
      main_url = "https://finance.yahoo.com/quote/TSLA"
      req = requests.get(main_url)
      soup = BeautifulSoup(req.text, "html.parser")
      ApplePrice = soup.find("fin-streamer", class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)")
      output = "Tesla Inc.(TSLA) today: $" + ApplePrice.text

      print(output)
      return output

def bitcoin_price():
    url = 'https://www.bitstamp.net/api/ticker/'
    response = requests.get(url)
    data = response.json()
    price = data['last']

    response =  "The current price of bitcoin is: $ " + str(price)

    print(response)
    return response

def eth_price():
    url = 'https://api.coingecko.com/api/v3/coins/ethereum'
    response = requests.get(url)
    data = response.json()
    price = data['market_data']['current_price']['usd']

    response =  "The current price of ethereum is: $ " + str(price)

    print(response)

    return response

def bnb_price():
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BNBETH'
    response = requests.get(url)
    data = response.json()
    price = data['price']

    response =  "The current price of BNB is: $ " + str(price)
    print(response)
    return response

def get_date_and_time():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(date_time)
    return date_time


if __name__ == '__main__':
    get_date_and_time()
    mondejar_weather()
    noticias()
    noticias_economicas()
    apple_price()
    tesla_price()
    bitcoin_price()
    eth_price()
    bnb_price()