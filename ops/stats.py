import coinmarketcapapi as c

"""
    In production environment: sandbox=False for CoinMarketCapAPI.
"""

coin = input("Enter your coin: ")

API_KEY = '6d7f5365-d3c4-4210-804e-c3c36302499d'
cmc = c.CoinMarketCapAPI(API_KEY, sandbox=False)

market = c.CoinMarketCap()
overall_data = market.stats(convert=coin)
coin_list = market.coin_list()
coin_detail = market.coin_ticker_detail(1, convert="CNY", disable_cache=False)

coin_data = {
    "info": cmc.cryptocurrency_info(symbol=coin),
    "map": cmc.cryptocurrency_map(symbol=coin),
    "latest_listing": cmc.cryptocurrency_listings_latest(symbol=coin),
    "market_pairs": cmc.cryptocurrency_market_pairs_latest(symbol=coin),
    "ohlcv": cmc.cryptocurrency_ohlcv_historical(symbol=coin),
    "quotes_latest": cmc.cryptocurrency_quotes_latest(symbol=coin),
    "quotes_historical": cmc.cryptocurrency_quotes_historical(symbol=coin),
    "exchange_info": cmc.exchange_info(symbol=coin),
    "exchange_map": cmc.exchange_map(symbol=coin),
    "exchange_listings": cmc.exchange_listings_latest(symbol=coin),
    "exchange_market_pairs": cmc.exchange_market_pairs_latest(symbol=coin),
    "exchange_quotes_latest": cmc.exchange_quotes_historical(symbol=coin),
    "exchange_quotes_historical": cmc.exchange_quotes_historical(symbol=coin),
    "global_metrics_quotes_latest": cmc.global_metrics_quotes_latest(symbol=coin),
    "global_metrics_quotes_historical": cmc.global_metrics_quotes_historical(symbol=coin),
    "tools_price_conversion": cmc.tools_price_conversion(symbol=coin)
}
