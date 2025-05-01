import requests 

api_key = "eaf68ffb413d707283399af330d02c3f"
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
print(response.json())
city2 = "Paris"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city2}&appid={api_key}&units=imperial"
response = requests.get(url)
# print(response)
# print(response.status_code)
weather = response.json()
print(weather)
print(weather["main"]["temp"])
print(weather["main"]["humidity"])
print(weather["visibility"])
print(weather["wind"]["speed"])
print(weather["sys"]["sunrise"])