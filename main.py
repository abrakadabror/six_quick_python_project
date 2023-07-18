import requests
import pandas as pd
from pprint import pprint

API_Key = '8c51483763c4a686fcaf0c855d616909'

city = input('enter a city: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_Key + '&q=' + city

response = requests.get(base_url)

if response.status_code == 200:
    print('good connection')
    weather_data = response.json()
#tworzenie slownika z danymi pogodowymi 
    weather_dict = {
    'City' : city,
    'Temperature': weather_data['main']['temp'],
    'Humidity': weather_data['main']['temp'],
    'Weather Description': weather_data['weather'][0]['description']
    }

    df = pd.DataFrame([weather_dict])
    print(df)
else:
    print('something went wrong') 



