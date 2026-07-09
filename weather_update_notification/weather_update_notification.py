import requests
from plyer import notification

# Get coordinates from city name
# user to enter city
city = input("Enter city name: ")
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = { "name": city, "count": 1}
geo_res =  requests.get(geo_url, geo_params).json()
geo_res = geo_res
#print(type(geo_res))

# check longitude and lattitude
if geo_res["results"] == []:
    print("city not found")
    exit()
else:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Get weather data from coordinates
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    weather_res = requests.get(weather_url, weather_params).json()
    #print(f"Current weather in {city}: {weather_res['current_weather']}")

    if current_weather := weather_res.get("current_weather"):
        temperature = current_weather.get("temperature")
        windspeed = current_weather.get("windspeed")
        weather_code = current_weather.get("weathercode")


        # Create a notification message
        message = f"Temperature: {temperature}°C\nWindspeed: {windspeed} km/h\nWeather Code: {weather_code}"

        # Send a notification
        notification.notify(
            title=f"Weather Update for {city}",
            message=message,
            timeout=10  # Notification will disappear after 10 seconds
        )

