import pika
import random

from db import DB


db = DB()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='data_trans')


def consume_data(channel, method, properties, body):
    img_url = body.decode('UTF-8')
    db.put(img_url)
    urls = list(db.get())
    print(urls)  # DEBUG
    print(random.choices(urls)[0]['url'])


channel.basic_consume(queue='data_trans', on_message_callback=consume_data, auto_ack=True)
channel.start_consuming()
