import json
import pika

if __name__ == '__main__':

    rabbitmq_ip = "localhost"
    rabbitmq_port = 5672
    # Queue name
    rabbitmq_queque = "CSC8112"

    def callback(ch, method, properties, body):
        data_dict = json.loads(body)
        print(f"Got message from producer msg: {data_dict}")
        data_list = [data_dict]
        with open("data.json", "w") as outfile:
            outfile.write(data_dict)

    # Connect to RabbitMQ service with timeout 1min
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_ip, port=rabbitmq_port, socket_timeout=60))
    channel = connection.channel()
    # Declare a queue
    channel.queue_declare(queue=rabbitmq_queque)

    channel.basic_consume(queue=rabbitmq_queque,
                          auto_ack=True,
                          on_message_callback=callback)

    channel.start_consuming()
