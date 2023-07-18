import requests
from pprint import pprint

API_Key = '8c51483763c4a686fcaf0c855d616909'

city = input('enter a city: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_Key + '&q=' + city

weather_data = requests.get(base_url).json()
pprint(weather_data)
