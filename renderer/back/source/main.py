import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='data_trans')


def consume_data(channel, method, properties, body):
    img_url = body.decode('UTF-8')
    print(img_url)  # ! DEBUG


channel.basic_consume(queue='data_trans', on_message_callback=consume_data, auto_ack=True)
channel.start_consuming()
