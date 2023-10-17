import json
import pika


class DataTransformer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='data_raw')
        self.channel.queue_declare(queue='data_trans')

    def transform_data(self, channel, method, properties, body):
        data = json.loads(body)
        print(data)  # ! DEBUG
        self.channel.basic_publish(exchange='', routing_key='data_trans', body=data['primaryImageSmall'])

    def start_transforming_data(self):
        self.channel.basic_consume(queue='data_raw', on_message_callback=self.transform_data, auto_ack=True)
        self.channel.start_consuming()
