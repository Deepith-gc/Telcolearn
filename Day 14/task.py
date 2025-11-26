import yaml

with open("C:/Users/deepi/Desktop/Telcolearn/Day 14/docker-compose-basic-nrf.yaml") as y:
    data = yaml.safe_load(y)


# for name, service in data["services"].items():
#     networks = service.get("networks", {})
#     ip = None
#     if networks:
#         ip = list(networks.values())[0].get("ipv4_address")
#     dep = service.get("depends_on", [])
#     dep_str = ", ".join(dep) if dep else "None"
    
#     print(f"{name} -> IP: {ip}, Depends on: {dep_str}")



# services = data.get("services",{}) 
# for service_name,service_data in services.items():
#     networks = service_data.get("networks",{})
#     for nw_name,nw_info in networks.items():
#         ip = nw_info.get("ipv4_address")
#         if ip:
#             print(f"{service_name}: {ip}")

# for service_name, service_data in services.items():
#     # Get dependencies
#     depends_on = service_data.get("depends_on", [])
#     depends_str = ", ".join(depends_on) if depends_on else "No dependencies"
    
#     print(f"Service {service_name} depends on: {depends_str}")






for name, service in data["services"].items():
    environment = service.get("environment", [])
    
    for env_var in environment:
        # env_var is a string like "MYSQL_USER=test"
        if '=' in env_var:
            key, value = env_var.split('=', 1)  # split only at the first '='
            if "PORT" in key.upper():  # only look for port-related variables
                print(f"{name} uses {key}={value}")
