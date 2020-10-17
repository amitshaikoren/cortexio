
## Client

The client is available as cortexio.client and exposes the following API:

```pycon
>>> from cortexio.client import upload_sample
>>> upload_sample(host= '127.0.0.1' , port= 8080 , sample_path= 'sample.mind.gz' )
```

And the following CLI:

```
$ python -m cortexio.client upload-sample \
-h/--host '127.0.0.1' \
-p/--port 8080 \
'snapshot.mind.gz'
…
```
