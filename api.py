import requests
import os 
from dotenv import load_dotenv
load_dotenv()

def get_coord(city_name):
    coord_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={os.getenv('API_key')}"
    response = requests.get(coord_url)
    return response.json()

def get_weather(lon, lat):
    main_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={os.getenv('API_key')}"
    response = requests.get(main_url)
    return response.json()



def main():

    city_name = input("Enter the name of the city: ")
    coord_details = get_coord(city_name)

    if not coord_details:
        print("City Not Found")
        return
    
    lon =  coord_details[0]["lon"]
    lat =  coord_details[0]["lat"]

    weather_details = get_weather(lon, lat)

    print(f"Temperature: {weather_details['main']['temp']} °C")
    print(f"Humidity: {weather_details['main']['humidity']} %")

if __name__ == '__main__':
    main()