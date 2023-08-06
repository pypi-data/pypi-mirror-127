import datetime

from .. import configuration
from .. import datastorage
from .. import logger
from .. import marketplace
from .. import triggers
from ..configuration import migrations
from ..historical import concrete
from ..telegram.logger import add_telegram_logger
from ..watchloop import TriggerLoop


def main(marketplace_name, keepalive, one_shot, dry_run):
    migrations.run_migrations()
    config = configuration.load_config()

    add_telegram_logger(config)
    if not one_shot:
        logger.info("Starting up …")

    datastore = datastorage.make_datastore(configuration.user_db_path)
    market = marketplace.make_marketplace(marketplace_name, config, dry_run)
    marketplace.check_and_perform_widthdrawal(market)

    if not one_shot:
        marketplace.report_balances(market, configuration.get_used_currencies(config))

    database_source = concrete.DatabaseHistoricalSource(
        datastore, datetime.timedelta(minutes=5)
    )
    crypto_compare_source = concrete.CryptoCompareHistoricalSource(
        config["cryptocompare"]["api_key"]
    )
    market_source = concrete.MarketSource(market)
    caching_source = concrete.CachingHistoricalSource(
        database_source, [market_source, crypto_compare_source], datastore
    )
    active_triggers = triggers.make_triggers(
        config, datastore, caching_source, market, dry_run
    )

    trigger_loop = TriggerLoop(active_triggers, config["sleep"], keepalive, one_shot)
    trigger_loop.loop()
