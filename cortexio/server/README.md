## Server

The server is available as cortexio.server and exposes the following API:

```pycon
>>> from cortexio.server import run_server
>>>run_server(host='0.0.0.0', port=8080, publish=None,mq_url="rabbitmq://0.0.0.0:5672/")
… # listen on host:port and pass received messages to publish
```

And in the following CLI:
```
$ python -m cortexio.server run-server \
-h/--host '0.0.0.0' \
-p/--port 8080 \
-h/--publish None \
'rabbitmq://0.0.0.0:5672/'
```
