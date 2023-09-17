#!/usr/bin/env python3
"""This module is an entrypoint which creates required instances and starts the server."""
import logging
import signal
import sys
from functools import partial
import prometheus_client
from flask import Flask, jsonify
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from server_thread import ServerThread
from service_parameters import RESPONSE_BODY, ServiceParameters


logger = logging.getLogger(__name__)

flask_app = Flask(__name__)
flask_app.data_provider = None


def register_prometheus_metrics_with_prefix(prefix: str):
    """Unregister default metrics and register a ProcessCollector with a prefix"""
    # Remove metrics without prefix
    prometheus_client.REGISTRY.unregister(prometheus_client.GC_COLLECTOR)
    prometheus_client.REGISTRY.unregister(prometheus_client.PLATFORM_COLLECTOR)
    prometheus_client.REGISTRY.unregister(prometheus_client.PROCESS_COLLECTOR)
    # Add process metrics (CPU and memory) with a prefix
    prometheus_client.ProcessCollector(namespace=prefix)

    flask_app.wsgi_app = DispatcherMiddleware(flask_app.wsgi_app, {
        '/metrics': prometheus_client.make_wsgi_app(),
    })


def main():
    """Create required instances and start the server."""
    try:
        service_params = ServiceParameters()
        register_prometheus_metrics_with_prefix(service_params.metrics_prefix)
        server = ServerThread(flask_app, service_params.api_port)
        server.start()
    except KeyboardInterrupt:
        sys.exit()
    except AssertionError as exc:
        sys.exit(f"The rule is violated: {type(exc)} - {exc}")
    except Exception as exc:
        sys.exit(f"An unexpected exception occurred: {exc}")

    signal.signal(signal.SIGTERM, partial(signal_handler, server=server))
    signal.signal(signal.SIGINT, partial(signal_handler, server=server))


def signal_handler(sig: int, frame=None, server: ServerThread = None):
    """Handle a signal and terminate the process."""
    try:
        server.shutdown()
    except Exception as exc:
        logger.warning("Failed to shutdown the server: %s", exc)

    sys.exit(sig)


@flask_app.route('/')
def api():
    """Response with static data."""
    response = jsonify(RESPONSE_BODY)
    response.status = 200

    return response


if __name__ == '__main__':
    main()
