import requests

def weather(location):

    url=f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid=5b79664c9c60e0ae848d0fd0f74dd42b'
    response = requests.get(url)
    data = response.json()

    weather={
    'high' : data['main']['temp'],
    'low' : data['main']['temp_min'],
    'feel' : data['main']['feels_like'],
    'humid' : data['main']['humidity']
     }

    return weather