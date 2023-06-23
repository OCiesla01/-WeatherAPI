import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

city = input("Enter the City: ")

url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city.title()}"

response = requests.get(url)


def get_data():
    location = response.json()['location']

    city = location['name']
    country = location['country']

    lat = location['lat']
    lon = location['lon']

    timezone = location['timezone_id']
    current_local_date = str(location['localtime']).split(" ")[0]
    current_local_time = str(location['localtime']).split(" ")[1]

    current = response.json()['current']

    observation_time = current['observation_time']

    temp_c = current['temperature']
    temp_f = (temp_c * 1.8) + 32

    weather_description = current['weather_descriptions']

    wind_speed = current['wind_speed']
    wind_direction = current['wind_dir']

    pressure = current['pressure']
    humidity = current['humidity']

    return f"""
        ====================================
        Checking time: {observation_time} UTC
        ------------------------------------
        {city}, {country}
        Latitude: {lat}\tLongitude: {lon}
        Time zone: {timezone}
        Current local date: {current_local_date}
        Current local time: {current_local_time}
        ------------------------------------
        Overall weather description: {weather_description[0]}
        Temperature: {temp_c}°C | {temp_f}°F
        Wind speed: {wind_speed}\tWind direction: {wind_direction}
        Pressure: {pressure}hPa | Humidity: {humidity}%
        ====================================
        """


try:
    print(get_data())
except KeyError:
    print(f"Sorry it seems like '{city}' is either not in the database or it does not exist.")
