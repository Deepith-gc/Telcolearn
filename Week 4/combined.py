import requests
import json
url1 = "https://api.open-meteo.com/v1/forecast?latitude=13.3145&longitude=76.257&daily=sunrise,sunset,weather_code&hourly=rain,relative_humidity_2m,cloud_cover&current=rain,is_day,cloud_cover&timezone=auto&past_days=3"
response1 = requests.get(url1)

url2 = "https://api.open-meteo.com/v1/forecast?latitude=14.48&longitude=78.8235&daily=sunrise,sunset,weather_code&hourly=rain,relative_humidity_2m,cloud_cover&current=rain,is_day,cloud_cover&timezone=auto&forecast_days=3"
response2 = requests.get(url2)

final_output = {
    "location_1": {
        "status": response1.status_code,
        "data": response1.json()
    },
    "location_2": {
        "status": response2.status_code,
        "data": response2.json()
    }
}
with open("merged.json","w") as file:
    file.write(json.dumps(final_output, indent=4))