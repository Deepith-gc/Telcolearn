import json

txt_file = "iplogs.txt"
json_file = "routes.json"

routes = []

with open(txt_file, "r") as file:
    for line in file:
        parts = line.split()
        route_dict = {}

        # First item is route or network
        route_dict["route"] = parts[0]

        # Extract key/value tokens
        i = 1
        while i < len(parts):
            if parts[i] in ["via", "dev", "proto", "scope", "src", "metric", "linkdown"]:
                if parts[i] == "linkdown":
                    route_dict["linkdown"] = True
                else:
                    route_dict[parts[i]] = parts[i+1]
                    i += 1
            i += 1

        routes.append(route_dict)

# Save JSON
json_data = json.dumps(routes, indent=4)
with open(json_file, "w") as f:
    f.write(json_data)

print("TXT routing table converted to JSON successfully!")
