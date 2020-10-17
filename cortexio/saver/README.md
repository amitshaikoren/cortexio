
## Saver

The saver is available as cortexio.saver and expose the following API:

```pycon
>>> from cortexio.saver import Saver
>>> saver = Saver(database_url)
>>> data = …
>>> saver.save( 'pose' , data)
```

Which connects to a database, accepts a topic name and some data, as consumed from the
message queue, and saves it to the database.

It is also provides the following CLI:

```pycon
$ python -m cortexio.saver save \
-d/--database 'postgresql://0.0.0.0:27017' \
'pose' \
'pose.result'
```

Which accepts a topic name and a path to some raw data, as consumed from the message
queue, and saves it to a database.

The CLI also supports running the saver as a service, which works with a message queue
indefinitely.

```pycon
$ python -m cortexio.saver run-saver \
'mongoDB://0.0.0.0:27017' \
'rabbitmq://0.0.0.0:5672/'
```
