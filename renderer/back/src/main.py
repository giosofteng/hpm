import pika
import random

from db import DB


db = DB()

parameters = pika.ConnectionParameters('localhost')  # ! DEBUG
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare('data_transformed')


def consume_data(channel, method, properties, body):
    url = body.decode('UTF-8')
    db.put(url)
    # ! DEBUG
    urls = list(db.get())
    print(urls)
    print(random.choices(urls)[0]['url'])


channel.basic_consume('data_transformed', consume_data, True)
channel.start_consuming()
