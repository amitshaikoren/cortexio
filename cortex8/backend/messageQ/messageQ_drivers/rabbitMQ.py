import pika


class rabbitMQ:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.name = f'RabbitMQ({host}:{port})'
        # TODO: implement try except for trying to establish a connection

    def publish(self, body):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = self.connection.channel()
        channel.queue_declare(queue=self.name)
        channel.basic_publish(exchange='',
                              routing_key=self.name,
                              body=body)
        connection.close()

    def consume(self):

