import yaml,json,logging

def parsing(filepath):
    with open("C:\\Users\\deepi\\Desktop\\3gpp\\src\\TS26510_Notifications.yaml","r") as file:
        data =yaml.safe_load(file)

    