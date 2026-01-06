import requests
import json
url = "https://api.open-meteo.com/v1/forecast?latitude=13.3145&longitude=76.257&daily=sunrise,sunset,weather_code&hourly=rain,relative_humidity_2m,cloud_cover&current=rain,is_day,cloud_cover&timezone=auto&past_days=3"
response = requests.get(url)
print("Status:", response.status_code)
print("Response:", response.json())
with open("loc1.json",'w') as file:
    json.dump(response.json(), file, indent=4)