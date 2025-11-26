import yaml
with open("C:/Users/deepi/Desktop/Telcolearn/Day 14/docker-compose-basic-nrf.yaml") as y:
    data = yaml.safe_load(y)

# print(data["services"]["oai-amf"]["environment"])    
# service=data["services"]["oai-amf"]
# list=service.get("environment",[])
# dict={}
# for i in list:
#     if "=" in i:
#         key,value=i.split("=",1)
#         dict[key]=value



# print("MCC =",dict.get("MCC"))
# print("MNC =",dict.get("MNC"))
