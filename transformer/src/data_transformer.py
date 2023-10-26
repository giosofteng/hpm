import json
import os
import pika
import requests


class DataTransformer:
    def __init__(self):
        url = os.environ.get('CLOUDAMQP_URL', 'rabbitmq')
        parameters = pika.URLParameters(url)
        parameters.socket_timeout = 5
        connection = pika.BlockingConnection(parameters)
        self.channel = connection.channel()
        self.channel.queue_declare('data_raw')
        self.channel.queue_declare('data_transformed')

    def transform_data(self, channel, method, properties, body):
        data = json.loads(body)
        # print(data)  # ! DEBUG
        url = data['primaryImageSmall']
        if url:
            response = requests.get(url)
            if response.status_code == 200:
                self.channel.basic_publish('', 'data_transformed', url.encode('UTF-8'))

    def start_transforming_data(self):
        self.channel.basic_consume('data_raw', self.transform_data, True)
        self.channel.start_consuming()
