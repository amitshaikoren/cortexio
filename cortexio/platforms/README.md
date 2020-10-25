## Platforms
This package provides platforms of different types: database, message queue, readers etc.

Each sub-package corresponds to a type of a platform. It consists of:
* A manager module that wrapps the shared api all the other drivers has to follow.
* A folder containing one or more driver implementation (.py files) that all follow the defined API by the manager class.

You can see an example for the message_queue platform folder hierarchy [here](messageQ)

Adding a new driver would be quite simple:
just add a new driver that implements the API defined by the manager class, and add a class attribute ```scheme``` with the name of the driver. <br>
All the rest is taken care of, and your new driver will be available for usage with the given name.


#### Example for of the `messageQ` platform:


MessageQManager implementation would look like:

```pycon
>>> drivers = load_drivers("messageQ_drivers")

>>>class MessageQManager:
...  def __init__(self, url):
...     parsed_url = urlparse(url)
...     self.host = parsed_url.hostname
...     self.port = parsed_url.port
...     self.scheme = parsed_url.scheme
...     self.driver = drivers[self.scheme](self.host, self.port)

... def publish(self, topic, handler):
...   self.driver.publish(topic, handler)

... def consume(self, topic, handler):
...     self.driver.consume(topic, handler)
```

Now, every driver would have to follow the ```publish```,```consume``` API.<br>
For example, rabbit_mq driver would look like:

```pycon
>>> class RabbitMq:
...     scheme = 'rabbitmq'
...    
...     def __init__(self, host, port):
...         self.host = host
...         self.port = port
...         ...
...    
...     def publish(self, topic, message):
...         ...
...    
...     def consume(self, topic, handler):
...         ...
```

And to use a message queue of type rabbitMQ:
```pycon
>>> from cortexio.platforms import MessageQManager
>>> url = 'rabbitmq://0.0.0.0:5672/'
>>> mq = MessageQManager(url)
>>> mq.publish(topic, message) # publish a given message on a given topic
``` 
