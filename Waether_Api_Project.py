# weather_api_project
import requests
#Ask user for a city name
city_name= input("city : ") 

#Your api key(repleace this with own if needed)
API_KEY = "220ed7caa53038b480eb7df1b612403d" 
# First API URL: Get the latitude and longitude for the entered city
URL = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}&units=metric"


response = requests.get(URL)
# Check if the request was successful and if any data was returned
if response.status_code == 200 and len(response.json()) > 0:
    city_data = response.json()[0]
    lat = city_data["lat"]
    lon = city_data["lon"]
    print(f"vazeiat : lat={lat}, lon={lon}")
else:
    print("Error !!! ", response.status_code)


#  Second API URL: Get the current weather using the coordinates
weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
weather_response = requests.get(weather_url)

# Chek if the weather request was successfull
if weather_response.status_code == 200:
    data = weather_response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    city = data["name"]

    print(f"Weather : {city}:")
    print(f"The temperature now : {temp}°C")
    print(f"ٌWeather condition : {desc}")
else:
    print("Error receving weather information !!! :(", weather_response.status_code)