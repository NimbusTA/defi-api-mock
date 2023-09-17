# nimbus-defi-api
The defi-api mock for the Nimbus protocol.

## How it works
Responses with static data at URL: `0.0.0.0:{API_PORT}/`.
Responses with Prometheus metrics at URL: `0.0.0.0:{API_PORT}/metrics`.

## Requirements
* Python 3.10


## Install
```shell
sudo apt-get install python3-dev python3-virtualvenv
python -m pip install --upgrade pip
pip install -r requirements.txt
```


## Run
The service receives its configuration parameters from environment variables. To start the service:
```shell
bash run.sh
```

To stop the service, send the SIGINT or SIGTERM signal to the process.


## Full list of configuration parameters
#### Optional
* `API_PORT` - The default value is `8000`.
* `LOG_LEVEL` - The logging level of the logging module: `DEBUG`, `INFO`, `WARNING`, `ERROR` or `CRITICAL`. The default level is `INFO`.
