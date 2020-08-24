from cortexio.platforms.messageQ.messageQ_drivers.rabbitMQ import RabbitMQ
if __name__=="__main__":
    mq = RabbitMQ(host="localhost", port="5672")
    mq.publish("hello")