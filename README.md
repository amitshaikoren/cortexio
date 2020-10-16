## cortexio

## Prerequisites

- [Python 3.8](https://www.python.org/downloads/release/python-382/)
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [docker-compose](https://docs.docker.com/compose/install/)

## Installation

1. Clone the repository and enter it:

    ```sh
    $ git clone git@github.com:amitshaikoren/cortexio.git
    ...
    $ cd cortexio
    ```

2. Run the installation script and activate the virtual environment:

    ```sh
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    [cortexio] $ # you're good to go!
    ```

3. To check that everything is working as expected, run the tests:

    ```sh
    [cortexio] $ pytest tests/
    ...
    ```
## Quickstart
After finishing the [installation](#installation) step, run the `run-pipeline` script to set up all the
necessary services:

```sh
[cortexio] $ ./scripts/run-pipeline.sh
...
# All dockers are up.
[cortexio] $
```

Please note that the first time set up may take some time.

#### Note: please make sure your user has docker permissions, otherwise you'll have to use the above commands with ```sudo```

Copy the desired binary sample you woul'd like to read from to the ```/data``` folder.
(if you'd like to use the full sample, you can download it from [here](https://storage.googleapis.com/advanced-system-design/sample.mind.gz)). <br>
For your convenience, a mini-sample is already available at the ```/data``` folder .

After that, upload some snapshots from the [client](/cortexio/client/README.md). <br>
For usage of the mini-sample provided:

```sh
[cortexio] $ python -m cortexio.client upload-sample ./cortexio/data/mini_sample.gz"
...
cortexio succeeded. All the 1 snapshots were uploaded!
[cortexio] $ 
```    
For usage of the a full sample (after it is copied to the ```/data``` folder:

```sh
[cortexio] $ python -m cortexio.client upload-sample --num-snaps 10 "./cortexio/data/sample.mind.gz"
...
cortexio succeeded. All the 10 snapshots were uploaded!
[cortexio] $ 
```    

#### Note:
If not necessary, try to use small values for the  ```--num-snaps``` parameter to ensure a smooth and fast flow.

Now you can use the [`cli`](/cortexio/cli/README.md) to consume the the data, or use the [`gui`](/cortexio/gui/README.md) to see an nice visualization of the data, in a website (default address will be: [http://localhost:8080](http://localhost:8080))

Finally, when your'e finished, you can shut down the pipline using:

```sh
[cortexio] $ ./scripts/stop-pipeline.sh
...
All dockers are stopped.
[cortexio] $
```

#### In case something goes wrong:
In rare cases some bugs may occur (due to things like enviorment or synchronization related stuff). <br>
A quick fix will be to delete the database contents and just trying to upload new snapshots.

Also, you can always try to restart the pipeline:

```sh
[cortexio] $ ./scripts/stop-pipeline.sh
...
All dockers are stopped.
[cortexio] $ ./scripts/run-pipeline.sh
...
All dockers are up.
[cortexio] $
```



## Project's Pipeline
![cortexio_pipeline](https://user-images.githubusercontent.com/37861691/82965333-79945680-9fd0-11ea-8e41-bbfb7f2e891b.png)

## Usage

The project contains one main package, `cortexio`, which contains several sub-packages.<br>
Each sub-package represents a micoservice of the project, which contains its own README file.<br>
For examples and further read:

* [`client`](/cortexiocortexiocortexiocortexio/client/README.md) - uploads snapshots to the server.
* [`server`](/cortexiocortexiocortexio/server/README.md) - receives the snapshots from the client, processes and publishes them to the [`MQ`](/cortexio/platforms/message_queue).
* [`parsers`](/cortexiocortexio/parsers/README.md) - consumes and parses the snapshots published by the server,and then publishing it back to the saver.
* [`saver`](/cortexio/saver/README.md) - consumes and saves the parsed data to the database.
* [`api`](/cortexiocortexiocortexio/server/README.md) - a REST API exposed to consume the data.
* [`cli`](/cortexiocortexio/cli/README.md) - a CLI that consumes the API.
* [`gui`](/cortexio/gui/README.md) - visualization of the data.
* [`platforms`](/cortexio/platforms/README.md) - several platforms that provide services to all the components

## Support

For contact please feel free to reach me on:
* Email - amitshaikoren@gmail.com 
