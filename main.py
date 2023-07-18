import requests
import datetime 
import pandas as pd
from pprint import pprint
import pytz


API_Key = '8c51483763c4a686fcaf0c855d616909'

city = input('enter a city: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_Key + '&q=' + city

response = requests.get(base_url)

if response.status_code == 200:
    print('good connection')
else:
    print('something went wrong') 

weather_data = response.json()
pprint(weather_data)
temp_kelvin  = weather_data['main']['temp'] #podajemy kolumne main oraz miejsce skad ma pobrac dane dla aktualnej temp
temp_celcius = temp_kelvin - 273.15
temp_round = round(temp_celcius, 2) #zaokroglamy wynik do dwoch miejsc po przecinku
temp_with_unit = str(temp_round) + '℃' #dodajemy jednostke celcjusz
#dodawanie inforamcji o jednostce cisnienia
pressure_unit = weather_data['main']['pressure']
pressure_with_unit = str(pressure_unit) + ' hPa' #dodajemy jednostke hPa

Humidity_opis = weather_data['main']['humidity'] 
Humidity_zachmurzenie = str(Humidity_opis) + '/zachmurzenie'

unix_timestamp = weather_data['sys']['sunset']
utc_time = datetime.datetime.utcfromtimestamp(unix_timestamp)
utc_time = utc_time.replace(tzinfo=pytz.utc)
local_timezone = pytz.timezone('Europe/Warsaw')  
warsaw_time = utc_time.astimezone(local_timezone).strftime('%Y-%m-%d %H:%M:%S')

sunset_time = warsaw_time


#tworzenie slownika z danymi pogodowymi 
weather_dict = {
    'City' : city,
    'Temperature': temp_with_unit,
    'Humidity': Humidity_zachmurzenie,
    'Weather Description': weather_data['weather'][0]['description'],
    'Actual_pressure': pressure_with_unit,
    'Localization': weather_data ['sys']['country'],
    'Power of wind': weather_data ['wind']['speed'],
    'Today sunset at': sunset_time
    }

df = pd.DataFrame([weather_dict])
print(df)

df.to_excel('weather_information.xlsx', index = False) #index false zeby nie dodalo nam kolumny z numerowaniem



