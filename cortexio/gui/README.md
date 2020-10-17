## GUI

### Implemenation details:


**Backend**: Flask and jinja templates <br>
**FrondEnd**: JS, Query, ajax, html, css


### Usage:

The GUI consumes the API and reflects it.

Usage as a python module:

``` pycon
>>> from cortexio.gui import run_gui_server
>>> run_gui_server(
... host = '127.0.0.1 ',
... port = 8080 ,
... api_url = '127.0.0.1:5000' ,
... )
```

Usage from CLI:

```pycon
$ python -m cortexio.gui run_gui_server \
-h/--host '127.0.0.1' \
-p/--port 8080 \
-H/--api_url '127.0.0.1:5000' \
```
