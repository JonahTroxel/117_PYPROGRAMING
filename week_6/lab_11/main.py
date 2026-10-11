_PATH_TO_WEATHER_JSON = "C:/Programming-2026-27/PYPROGRAM-2026-27/week_6/lab_11/weather.json"

import json

with open(_PATH_TO_WEATHER_JSON, "r") as file:
    weather_data = json.load(file)
print("Welcome to the Weather app")
print("choose a location:")
for index, location in enumerate(weather_data):
    print(f"{index + 1}. {location['Location']}")

choice = int(input("Enter the number of your choice: ")) - 1
selected_location = weather_data[choice]
print(f"The weather in {selected_location['Location']} is {selected_location['Weather']}.")