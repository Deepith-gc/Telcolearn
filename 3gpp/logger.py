import logging,json

logging.basicConfig(filename='obs.log',level=logging.INFO,)

def log_event(event,data):
    logging.info(json.dumps({"event":event,"data":data}))
try:
    data = json.load(r"C:\Users\deepi\Desktop\3gpp\src\TS26510_Notifications.yaml")
except Exception as e:
    log_event("failed_attempt","could not fetch data")
    logging.warning("Unsuccessful")