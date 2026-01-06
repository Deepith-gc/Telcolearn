import yaml, json
with open("C:/Users/deepi/Desktop/Telcolearn/Day 14/docker-compose-basic-nrf.yaml") as f:
    y = yaml.safe_load(f)

json_data = json.dumps(y,indent=2)
print(json_data)