from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
# load_dotenv()

def index(request):
    CITY_NAME = 'Austin'
    API_KEY = os.getenv('OPENWEATHERMAP_API_KEY', None)
    if (API_KEY):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}'
        print(url)
        city_weather = requests.get(url).json() 
        print(city_weather)
    else:
        from .openweathermap_data import test_city_weather
        city_weather = test_city_weather

    weather = {
        'city': city_weather['name'],
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon'],
        'feels_like': city_weather['main']['feels_like'],
        'pressure': city_weather['main']['pressure'],
        'humidity': city_weather['main']['humidity'],
        'rain': city_weather['rain']['1h'] if 'rain' in city_weather and '1h' in city_weather['rain'] else '0',
        'clouds': city_weather['clouds']['all']
    }

    context = {'weather' : weather}
    
    return render(request, 'weather/index.html', context) 