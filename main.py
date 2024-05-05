import serial
import pprint
import json

from utils import select_port, treat_data
from server.grafana_api import PrometheusAPI


def load_credentials():
    with open(".credentials.json", 'r') as file:
        aux_credentials = file.read()
    credentials = json.loads(aux_credentials)
    return credentials["API_ID"], credentials["API_TOKEN"]


baud_rate = 9600 # 115200
serial_port = '/dev/ttyUSB0' #if this does not work choose the select port option
#serial_port = select_port()

ENDPOINT = "https://influx-prod-24-prod-eu-west-2.grafana.net/api/v1/push/influx/write"
API_ID, API_TOKEN = load_credentials() 


def main():
    sendAPI = True
    print_info_sent = True
    api = PrometheusAPI(API_ID, API_TOKEN, ENDPOINT)

    try:
        ser = serial.Serial(serial_port, baud_rate)
        dataSend = {}  
        
        while True:
            dataRecieved = ser.readline().decode().strip()
            if dataRecieved:
                dataRecieved = dataRecieved.split()
                if dataRecieved == ["end"]:
                    treated_data = treat_data(dataSend)
                    if sendAPI:
                        api.send_to_grafana(treated_data)
                    if print_info_sent:
                        pprint.pprint(treated_data)
                    dataSend = {}
                else:
                    #print(dataRecieved)
                    dataSend[dataRecieved[0]] = dataRecieved[1]

    except Exception as e:
        # print("Failed to open serial port:", serial_port)
        print("Raised exception: " + str(e))


if __name__ == "__main__":
    main()
    
