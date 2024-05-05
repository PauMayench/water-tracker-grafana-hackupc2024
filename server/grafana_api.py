import requests
import base64
import logging
import json


# Logger format + initialization
log_format = "%(asctime)s - PROMETHEUS_API - [%(levelname)s] : %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format, datefmt='%Y-%m-%d %H:%M:%s')

# Store sensor names + associated labels to parse the query
sensor_dict = {
    "temperature": ["temp", "label=temperature"],
    "humidity": ["humid", "label=humidity"],
    "level_lake1": ["lake", "label=Sau"],
    "level_lake2": ["lake", "label=Baells"],
    "level_lake3": ["lake", "label=Rialb"],
    "level_lake4": ["lake", "label=Canelles"],
    "level_lake5": ["lake", "label=Susqueda"],
    "lightness":  ["light", "label=lightness"],
    "consum":  ["cons", "label=consum"],
}


class PrometheusAPI:
    def __init__(self, _id, _key, _endpoint):
        self.id = _id
        self.key = _key
        self.endpoint = _endpoint

    def send_data(self, body):
        '''
        "test,bar_label=abc,source=grafana_cloud_docs metric=777"
        '''
        response = requests.post(self.endpoint, 
                                 headers = {'Content-Type': 'text/plain'},
                                 data = str(body),
                                 auth = (self.id, self.key)
        )
        return response.status_code, response.text

    def parse_query(self, sensor_input):
        '''
        "temperature,label=temperature, metric=XYZ"
        '''
        query = ""
        separator = '\n'
        for sensor in sensor_input:
            metric_labels = ','.join(sensor_dict[sensor])
            sensor_metric = sensor_input[sensor]
            query += f"{metric_labels} metric={sensor_metric}{separator}"
        return query

    def send_to_grafana(self, sensor_input):
        '''
        sample -> "soil_humidity,plant=rose metric=0.88\n soil_temperature,plant=rose metric=69"
        '''
        try:
            query = self.parse_query(sensor_input)
            ret_code, ret_data = self.send_data(query)
            logging.info(f"Sensor data sent successfully -> Response: <{str(ret_code)}, \"{str(ret_data)}\">")

        except Exception as e:
            logging.error(e)



