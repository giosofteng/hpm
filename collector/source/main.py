import json
import pika

# from data_collector import DataCollector


if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='data')

    def callback(ch, method, properties, body):
        data = json.loads(body)
        print(data)

    channel.basic_consume(queue='data', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

    # data_collector = DataCollector()
    # data_collector.start_data_collection()
