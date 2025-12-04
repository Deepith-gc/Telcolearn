import requests
import json
url = "https://api.open-meteo.com/v1/forecast?latitude=14.48&longitude=78.8235&daily=sunrise,sunset,weather_code&hourly=rain,relative_humidity_2m,cloud_cover&current=rain,is_day,cloud_cover&timezone=auto&forecast_days=3"
response = requests.get(url)
print("Status:", response.status_code)
print("Response:", response.json())
with open("loc2.json",'w') as file:
    json.dump(response.json(), file, indent=4)