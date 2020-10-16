## API

The API is available as cortexio.api and expose the following API:

```pycon
>>> from cortexio.api import run_api_server
>>> run_api_server(
... host = "http://127.0.0.1/" ,
... port = 7000 ,
... database_url = "mongodb://127.0.0.1:27017" ,
... )
… # listen on host : port and serve data from database_url
```

And the following CLI:

```
python -m cortexio.api run-server \
-h/--host '127.0.0.1' \
-p/--port 7000 \
-d/--database 'postgresql://127.0.0.1:27017'
```

The API server supports the following RESTful API endpoints:

- **127.0.0.1:27017 /users** - Returns the list of all the supported users, including their IDs and names only.
- **127.0.0.1:27017 /users/ user-id** - Returns the specified user's details: ID, name, birthday and gender.
- **127.0.0.1:27017 /users/ user-id /snapshots** - Returns the list of the specified user's snapshot IDs and datetimes only.
- **127.0.0.1:27017 /users/ user-id /snapshots/ snapshot-id** - Returns the specified snapshot's details: ID, datetime, and the available results'
names only (e.g. pose ).
- **127.0.0.1:27017 /users/ user-id /snapshots/ snapshot-id / result-name** - Returns the specified snapshot's results.
