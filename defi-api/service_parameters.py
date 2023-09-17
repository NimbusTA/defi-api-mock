"""This module contains the ServiceParameters class implementation and constants."""
import logging
import os

import log

logger = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = 'INFO'
DEFAULT_API_PORT = '8000'
DEFAULT_PROMETHEUS_METRICS_PREFIX = 'defi_api_'


class ServiceParameters:
    """This class contains the service parameters and methods to check and parse them."""
    api_port: int
    metrics_prefix: str

    def __init__(self):
        log_level = os.getenv('LOG_LEVEL', DEFAULT_LOG_LEVEL)
        self._check_log_level(log_level)
        log.init_log(log_level)

        logger.info("Checking configuration parameters")

        logger.info("[ENV] LOG_LEVEL: %s", log_level)

        logger.info("[ENV] Get 'API_PORT'")
        self.api_port = int(os.getenv('API_PORT', DEFAULT_API_PORT))
        logger.info("[ENV] 'API_PORT': %s", self.api_port)

        logger.info("[ENV] Get 'PROMETHEUS_METRICS_PREFIX'")
        self.metrics_prefix = os.getenv('PROMETHEUS_METRICS_PREFIX', DEFAULT_PROMETHEUS_METRICS_PREFIX)
        logger.info("[ENV] 'PROMETHEUS_METRICS_PREFIX': %s", self.metrics_prefix)

        logger.info("Successfully checked configuration parameters")

    @staticmethod
    def _check_log_level(log_level: str):
        """Check the logger level based on the default list."""
        log_levels = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
        if log_level not in log_levels:
            raise ValueError(f"Valid 'LOG_LEVEL_STDOUT' values: {log_levels}")


RESPONSE_BODY = {
    "status": 0,
    "message": "OK",
    "data": {
        "nProjects": 6,
        "projects": [
            {
                "projectId": 1,
                "projectName": "Curve",
                "projectType": "DEX",
                "compound": False,
                "token1Name": "xcDOT",
                "token2Name": "nDOT",
                "tokenItemCaption": "xcDOT-nDOT",
                "buttons": [
                    {
                        "caption": "Add liquidity",
                        "link": "#"
                    },
                    {
                        "caption": "Swap",
                        "link": "#"
                    }
                ],
                "isActive": True,
                "interestRate": "10.02",
                "tvl": 2716787.9047005186,
                "incentiveTokenNames": [],
                "incentiveTokenAmounts": []
            },
            {
                "projectId": 2,
                "projectName": "Beefy",
                "projectType": "Farm",
                "compound": True,
                "token1Name": "xcDOT-nDOT",
                "token2Name": None,
                "tokenItemCaption": "Curve xcDOT-nDOT",
                "buttons": [
                    {
                        "caption": "Deposit",
                        "link": "#"
                    }
                ],
                "isActive": True,
                "interestRate": "10.02",
                "tvl": 244272.76985017065,
                "incentiveTokenNames": [],
                "incentiveTokenAmounts": []
            },
            {
                "projectId": 3,
                "projectName": "StellaSwap",
                "projectType": "DEX",
                "compound": False,
                "token1Name": "xcDOT",
                "token2Name": "nDOT",
                "tokenItemCaption": "xcDOT-nDOT",
                "buttons": [
                    {
                        "caption": "Add liquidity",
                        "link": "#"
                    },
                    {
                        "caption": "Swap",
                        "link": "#"
                    }
                ],
                "isActive": True,
                "interestRate": "10.85",
                "tvl": 1122113.1822753097,
                "incentiveTokenNames": [
                    "STELLA",
                    "WGLMR"
                ],
                "incentiveTokenAmounts": [
                    "3163.63",
                    "52.80"
                ]
            },
            {
                "projectId": 4,
                "projectName": "BeamSwap",
                "projectType": "DEX",
                "compound": False,
                "token1Name": "xcDOT",
                "token2Name": "nDOT",
                "tokenItemCaption": "xcDOT-nDOT",
                "buttons": [
                    {
                        "caption": "Add liquidity",
                        "link": "#"
                    },
                    {
                        "caption": "Swap",
                        "link": "#"
                    }
                ],
                "interestRate": "4.13",
                "tvl": 392187.6527884675,
                "incentiveTokenNames": [
                    "GLINT"
                ],
                "incentiveTokenAmounts": [
                    "36720.00"
                ]
            },
            {
                "projectId": 5,
                "projectName": "Beefy",
                "projectType": "Farm",
                "compound": True,
                "token1Name": "xcDOT-nDOT",
                "token2Name": None,
                "tokenItemCaption": "StellaSwap xcDOT-nDOT",
                "buttons": [
                    {
                        "caption": "Deposit",
                        "link": "#"
                    }
                ],
                "isActive": True,
                "interestRate": "7.86",
                "tvl": 450980.70845176966,
                "incentiveTokenNames": [],
                "incentiveTokenAmounts": []
            },
            {
                "projectId": 6,
                "projectName": "Beefy",
                "projectType": "Farm",
                "compound": True,
                "token1Name": "xcDOT-nDOT",
                "token2Name": None,
                "tokenItemCaption": "Beamswap xcDOT-nDOT",
                "buttons": [
                    {
                        "caption": "Deposit",
                        "link": "#"
                    }
                ],
                "isActive": True,
                "interestRate": "3.67",
                "tvl": 244683.4556736184,
                "incentiveTokenNames": [],
                "incentiveTokenAmounts": []
            },
            {
                "projectId": 7,
                "projectName": "MAI",
                "projectType": "Stablecoin",
                "compound": True,
                "token1Name": "nDOT",
                "token2Name": None,
                "tokenItemCaption": "MAI",
                "buttons": [
                    {
                        "caption": "Create vault",
                        "link": "#"
                    }
                ],
                "isActive": True,
                "interestRate": "12.3",
                "tvl": 123456.123456,
                "incentiveTokenNames": [],
                "incentiveTokenAmounts": []
            },
            {
                "projectId": 8,
                "projectName": "Moonwell",
                "projectType": "Lending",
                "compound": True,
                "token1Name": "nDOT",
                "token2Name": None,
                "tokenItemCaption": "mnDOT",
                "buttons": [
                    {
                        "caption": "Deposit",
                        "link": "#"
                    }
                ],
                "isActive": True,
                "interestRate": "12.3",
                "tvl": 123456.123456,
                "incentiveTokenNames": [],
                "incentiveTokenAmounts": []
            }
        ]
    }
}
