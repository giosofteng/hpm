import json
import pika


class DataTransformer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='data')

    def transform_data(self, channel, method, properties, body):
        # ! PLACEHOLDER CODE
        data = json.loads(body)
        print(data)

    def start_transforming_data(self):
        self.channel.basic_consume(queue='data', on_message_callback=self.transform_data, auto_ack=True)
        self.channel.start_consuming()
