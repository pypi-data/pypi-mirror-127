"""Submits three month rolling average of the USPCE to TellorX on Rinkeby."""
import asyncio
from typing import Optional

from telliot_core.apps.telliot_config import TelliotConfig
from telliot_core.contract.contract import Contract
from telliot_core.utils.abi import rinkeby_tellor_master
from telliot_core.utils.abi import rinkeby_tellor_oracle

from telliot_feed_examples.feeds.uspce import uspce_feed
from telliot_feed_examples.reporters.interval import IntervalReporter


def get_cfg() -> TelliotConfig:
    """Get rinkeby endpoint from config

    If environment variables are defined, they will override the values in config files
    """
    cfg = TelliotConfig()

    # Override configuration for rinkeby testnet
    cfg.main.chain_id = 4

    _ = cfg.get_endpoint()

    return cfg


def get_master(cfg: TelliotConfig) -> Optional[Contract]:
    """Helper function for connecting to a contract at an address"""
    endpoint = cfg.get_endpoint()
    if not endpoint:
        print("Could not connect to master contract.")
        return None

    endpoint.connect()
    master = Contract(
        address="0x657b95c228A5de81cdc3F85be7954072c08A6042",
        abi=rinkeby_tellor_master,  # type: ignore
        node=endpoint,
        private_key=cfg.main.private_key,
    )
    master.connect()
    return master


def get_oracle(cfg: TelliotConfig) -> Optional[Contract]:
    """Helper function for connecting to a contract at an address"""
    endpoint = cfg.get_endpoint()
    if not endpoint:
        print("Could not connect to master contract.")
        return None

    if endpoint:
        endpoint.connect()
    oracle = Contract(
        address="0x07b521108788C6fD79F471D603A2594576D47477",
        abi=rinkeby_tellor_oracle,  # type: ignore
        node=endpoint,
        private_key=cfg.main.private_key,
    )
    oracle.connect()
    return oracle


if __name__ == "__main__":
    cfg = get_cfg()

    master = get_master(cfg)
    oracle = get_oracle(cfg)

    rinkeby_endpoint = cfg.get_endpoint()

    uspce_reporter = IntervalReporter(
        endpoint=rinkeby_endpoint,
        private_key=cfg.main.private_key,
        master=master,
        oracle=oracle,
        datafeeds=[uspce_feed],
    )

    _ = asyncio.run(uspce_reporter.report_once())  # type: ignore
