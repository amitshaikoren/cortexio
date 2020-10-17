#!/bin/bash
python -m cortexio.server run-server "rabbitmq://0.0.0.0:5672" &
python -m cortexio.parsers run-parsers &
python -m cortexio.saver run-saver "mongodb://0.0.0.0:27017" "rabbitmq://0.0.0.0:5672" &
python -m cortexio.api run-server &
python -m cortexio.gui run-server &
