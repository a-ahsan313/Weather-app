import requests
import json

city = input("Enter the name of the city: ")

result = requests.get(url=f'https://api.weatherapi.com/v1/current.json?key=YOUR API={city}')

# print(result.text)
weather_dic = json.loads(result.text)
print(f"\nCity: {weather_dic['location']['name']}")
print(f"Country: {weather_dic['location']['country']}")
print(f"Temperature: {weather_dic['current']['temp_c']}\n")

