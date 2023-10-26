import os
import pika
# import random  # ! DEBUG


class AMQP:
    def __init__(self, db):
        self.db = db

        url = os.environ.get('CLOUDAMQP_URL', 'rabbitmq')
        parameters = pika.URLParameters(url)
        parameters.socket_timeout = 5
        connection = pika.BlockingConnection(parameters)
        self.channel = connection.channel()
        self.channel.queue_declare('data_transformed')

    def store_data(self, channel, method, properties, body):
        url = body.decode('UTF-8')
        self.db.put(url)
        # ! DEBUG
        # urls = list(self.db.get())
        # print(urls)
        # print(random.choices(urls)[0]['url'])

    def start_storing_data(self):
        self.channel.basic_consume('data_transformed', self.store_data, True)
        self.channel.start_consuming()
