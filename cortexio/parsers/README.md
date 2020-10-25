
## Parsers

### Usage

The parsers are available as cortexio.parsers and exposes the following API:

```pycon
>>> from cortexio.parsers import run_parser
>>> data = …
>>> result = run_parser( 'pose' , data)
```

Which accepts a parser name and some raw data, as consumed from the message queue, and returns the result, as published to the message queue.

It also provides the following CLI:

``` python -m cortexio.parsers parse 'pose' 'snapshot.raw' > 'pose.result' ```

Which accepts a parser name and a path to some raw data, as consumed from the message
queue, and prints the result, as published to the message queue (optionally redirecting it
to a file).

The CLI should also support running the parsers as a service, which works with a message queue indefinitely.

```$ python -m cortexio.parsers run-parser 'pose' 'rabbitmq://127.0.0.1:5672/' ```

### Default available parsers

The default implemented parsers in the project are:
* [pose parser](parser_drivers/pose.py)
* [feeling parser](parser_drivers/feelings.py)
* [color-image parser](parser_drivers/color_image.py)
* [depth-image parser](parser_drivers/depth_image.py)

### Package implementation

The parsers package structure is the same as any other [platform](../platforms/README.md).
It consists of a ```parser_manager.py``` file, that gathers all the common logic for the parsers and manages the communication with the message queue. <br>
It also consists of a drivers folder called ``` parser_drivers ``` which contains all the available parsers.  


### Adding a new parser

Adding a new parser would be quite simple: just add a new .py file under the  ``` parser_drivers ``` folder,
and implement a class with the following interface:

```pycon
class LoveParser:
    scheme = "love"

    @staticmethod
    def parse(snapshot):
            ...
            # parsing stuff blah blah blah i'm parsing 010101
            ...
```
Note that parse accepts as an argument a snapshot. <br>
You will also required to add a  ```scheme``` with the name of the parser so the ```load_drivers``` fuction would know to collect the parser function, with a proper name.
