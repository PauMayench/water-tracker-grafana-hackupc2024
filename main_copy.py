import serial
from utils import select_port, treat_data
from server.grafana_api import PrometheusAPI
import time
import random

def load_credentials():
    with open(".credentials.json", 'r') as file:
        aux_credentials = file.read()
    credentials = json.loads(aux_credentials)
    return credentials["API_ID"], credentials["API_TOKEN"]



USER_ID, API_KEY = load_credentials() 
ENDPOINT = "https://influx-prod-24-prod-eu-west-2.grafana.net/api/v1/push/influx/write"


api = PrometheusAPI(USER_ID, API_KEY, ENDPOINT)

sample = {
    "temperature": 25, 
    "humidity": 30, 
    "level_lake1": 700,
    "level_lake2": 312, 
    "level_lake3": 132,
    "level_lake4": 53 
}



dataSend = {}  
while True:

    rand_sample = {
        "temperature": random.randint(15, 30), 
        "humidity": random.randint(20, 60), 
        "level_lake1": random.randint(10,34),
        "level_lake2": random.randint(20,70), 
        "level_lake3": random.randint(5,15),
        "level_lake4": random.randint(40,67),
        "level_lake5": random.randint(0,100),
        "consum": random.randint(10,40),
    }
    api.send_to_grafana(rand_sample)

    time.sleep(5)



