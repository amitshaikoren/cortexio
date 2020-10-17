## CLI

The CLI consumes the [API](../api/README.md), and quite simply — reflects its:

```
$ python -m cortexio.cli get-users
…
$ python -m cortexio.cli get-user 1
…
$ python -m cortexio.cli get-snapshots 1
…
$ python -m cortexio.cli get-snapshot 1 2
…
$ python -m cortexio.cli get-result 1 2 'pose'
…
```

All commands accept the -h/--host and -p/--port flags to configure the host andport, but default to the API's address. <br>
The get-result should also accept the -s/--save flag that receives a path, and saves the result's data to that path.
