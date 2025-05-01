
# Making a basic API request
import requests

# Set up our request
# api_key = 'eaf68ffb413d707283399af330d02c3f'
# api_key = "d3f36b82390abaef4d1342b0555c5172"
# weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
url = f'https://api.openweathermap.org/data/2.5/weather'


# Parameters for our request
parameters = {
    "q": "Cadiz, Spain",         # The city we want weather for
    "appid": api_key,    # API key (we'll discuss this)
    "units": "metric"           # Get temperature in Celsius
}

# Make the request
response = requests.get(url, params=parameters)

# Check if request was successful
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()
    
    # Extract and display some data
    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    weather = weather_data["weather"][0]["description"]
    
    print(f"Current weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Conditions: {weather}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)




