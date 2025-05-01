import json 

shopping_list = [
    ['mangos', 'apples', 'oranges', 'grapes'],
    ['carrots', 'broccoli', 'lettuce'],
    ['corn flakes', 'oatmeal']
]

print("Shopping list by category:")
print(shopping_list)

# Accessing Data in Nested Lists:
# Access a specific item
item = shopping_list[0][1]
print("\nThe second item in the first category is:", item)  # apples

# Access the last category
last_category = shopping_list[-1]
print("Last category:", last_category)  # ['corn flakes', 'oatmeal']

# Modifying Nested Lists:
# Add an item to the first category
shopping_list[0].append('bananas')
print("\nAdded bananas to first category:", shopping_list[0])

# Replace an item in the second category
shopping_list[1][0] = 'baby carrots'
print("Updated second category:", shopping_list[1])

# Add a whole new category
shopping_list.append(['milk', 'cheese', 'yogurt'])
print("Added a new category:", shopping_list[-1])

# Iterating Through Nested Lists:
# Loop through all items in the shopping list
print("\nAll shopping list items:")
for category in shopping_list:
    for item in category:
        print(f"- {item}")

# Loop with a counter
print("\nNumbered shopping list:")
counter = 1
for category in shopping_list:
    for item in category:
        print(f"{counter}. {item}")
        counter += 1

# Filter items containing 'a'
print("\nItems containing 'a':")
for category in shopping_list:
    for item in category:
        if 'a' in item:
            print(f"- {item}")




# NEW


student_data = {
    'name': 'Alice Johnson',
    'age': 22,
    'courses': ['Python Programming', 'Data Structures', 'Algorithms'],
    'grades': {
        'Python Programming': 95,
        'Data Structures': 88,
        'Algorithms': 91
    },
    'contact': {
        'email': 'alice@example.com',
        'phone': '555-123-4567',
        'address': {
            'street': '123 Campus Dr',
            'city': 'University Town',
            'state': 'CA',
            'zip': '94305'
        }
    }
}

# Convert to JSON string
json_data = json.dumps(student_data, indent=4)
print("\nJSON representation of student data:")
print(json_data)

# Convert JSON string back to Python
python_data = json.loads(json_data)
print("\nConverted back to Python:")
print(type(python_data))

# Read/write JSON to a file
with open('student.json', 'w') as f:
    json.dump(student_data, f, indent=4)

print("\nWritten to student.json")

with open('student.json', 'r') as f:
    loaded_data = json.load(f)

print("Successfully loaded from file")

Real-World Example - API Data:
# Sample API response for a weather service
weather_api_response = {
    "location": {
        "name": "New York",
        "region": "New York",
        "country": "United States",
        "lat": 40.71,
        "lon": -74.01,
        "timezone": "America/New_York"
    },
    "current": {
        "temp_f": 72.5,
        "condition": {
            "text": "Partly cloudy",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png"
        },
        "humidity": 65,
        "wind_mph": 10.5,
        "precip_in": 0.0
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2025-04-08",
                "day": {
                    "maxtemp_f": 75.6,
                    "mintemp_f": 62.1,
                    "condition": {
                        "text": "Sunny",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png"
                    }
                },
                "hour": [
                    {"time": "2025-04-08 00:00", "temp_f": 65.3},
                    {"time": "2025-04-08 01:00", "temp_f": 64.8},
                    {"time": "2025-04-08 02:00", "temp_f": 64.0}
                ]
            },
            {
                "date": "2025-04-09",
                "day": {
                    "maxtemp_f": 78.2,
                    "mintemp_f": 63.5,
                    "condition": {
                        "text": "Cloudy",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/119.png"
                    }
                },
                "hour": [
                    {"time": "2025-04-09 00:00", "temp_f": 66.2},
                    {"time": "2025-04-09 01:00", "temp_f": 65.7},
                    {"time": "2025-04-09 02:00", "temp_f": 65.1}
                ]
            }
        ]
    }
}

# Extract and display weather information
location_name = weather_api_response["location"]["name"]
current_temp = weather_api_response["current"]["temp_f"]
current_condition = weather_api_response["current"]["condition"]["text"]

print(f"\nCurrent weather in {location_name}: {current_temp}°F, {current_condition}")

# Process forecast data
print("\nForecast:")
for day in weather_api_response["forecast"]["forecastday"]:
    date = day["date"]
    max_temp = day["day"]["maxtemp_f"]
    min_temp = day["day"]["mintemp_f"]
    condition = day["day"]["condition"]["text"]
    
    print(f"{date}: {min_temp}°F to {max_temp}°F, {condition}")




NEW





















