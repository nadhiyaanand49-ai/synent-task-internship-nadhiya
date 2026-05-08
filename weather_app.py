import requests

# Enter your API key here
API_KEY = "448c7419950e8a7f3b098752114c1125"


# User input
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Request data
response = requests.get(url)

# Convert to JSON
weather_data = response.json()

# Check city exists
if response.status_code == 200:

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    condition = weather_data['weather'][0]['description']

    print("\n===== WEATHER DETAILS =====")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")

else:
    print("Invalid city name or API issue.")