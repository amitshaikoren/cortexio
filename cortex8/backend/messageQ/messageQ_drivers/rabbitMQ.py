import pika


class RabbitMQ:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.name = f'RabbitMQ({host}:{port})'
        # TODO: implement try except for trying to establish a connection

    def publish(self, body):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()
        channel.queue_declare(queue=self.name)

        channel.basic_publish(exchange='',
                              routing_key=self.name,
                              body=body)

        connection.close()

    def consume(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()
        channel.queue_declare(queue=self.name)

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        channel.basic_consume(queue=self.name,
                              auto_ack=True,
                              on_message_callback=callback)

        channel.start_consuming()


if __name__ == "__main__":
    mq = RabbitMQ(host="localhost", port="5672")
    mq.consume()
    mq.publish("hello")
