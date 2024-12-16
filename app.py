import requests

API_KEY = 'f988a0df9f45e06f1d3844c44a66cdf8'  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/"


def get_current_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "main" in data:
            weather = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather
        else:
            # Print the whole response to understand why "main" is missing
            print(f"Error: The 'main' key is missing in the response. Full response: {data}")
            return None
    else:
        print(f"Error fetching current weather for {city}: {response.status_code}")
        print(response.json())  # Print error message from the API response
        return None


def display_weather(city):
    """Display the current weather """
    current_weather = get_current_weather(city)
    if current_weather:
        print(f"Weather in {city}:")
        print(f"Temperature: {current_weather['temperature']}°C")
        print(f"Description: {current_weather['description']}")
        print(f"Humidity: {current_weather['humidity']}%")
        print(f"Wind Speed: {current_weather['wind_speed']} m/s")
    else:
        print("City not found. Please check the name and try again.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather(city)