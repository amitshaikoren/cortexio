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
