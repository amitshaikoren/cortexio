#!/bin/bash
python -m cortexio.server run-server "rabbitmq://127.0.0.1:5672" &
python -m cortexio.parsers run-parsers &
python -m cortexio.saver run-saver "mongodb://127.0.0.1:27017" "rabbitmq://0.0.0.0:5672" &
python -m cortexio.api run-server &
python -m cortexio.gui run-server &
