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
... host = '0.0.0.0 ',
... port = 8080 ,
... api_url = '0.0.0.0:5000' ,
... )
```

Usage from CLI:

```pycon
$ python -m cortexio.gui run_gui_server \
-h/--host '0.0.0.0' \
-p/--port 8080 \
-H/--api_url '0.0.0.0:5000' \
```
