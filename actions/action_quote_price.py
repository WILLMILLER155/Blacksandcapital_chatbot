import requests


def quotes(ticker):

    url = 'http://api.marketstack.com/v1/intraday?access_key=74fab9f9b749678d85ed28326e5d5702&symbols=' + ticker

    response = requests.get(url)
    data = response.json()

    quote = data['data'][0]['open']

    return str(quote)

