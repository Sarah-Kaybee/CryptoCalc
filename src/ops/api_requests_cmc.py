import coinmarketcapapi as c

"""
APICoinData:
    Class designed to format data specifically for views.
    Generates two JSON objects: coins_static and coins_dynamic.
    
    COINS_STATIC: Updated every 1 day. Variables that rarely change for any coin.
    coins_static = 
    {
        { "coin_id_1": 
            {
                "name": Bitcoin,
                "symbol": BTC,
                "logo": img reference,
                "date_added": datetime,
                "farm_type": mining,
            }
        },
        ...
        { more coin objects }
    }
    
    COINS_DYNAMIC: Updated every 5 minutes. 
    Variables that constantly change and need to be updated in the UI.
    coins_dynamic = 
    {
        { "coin_id_1": 
            {
                "price": 29049062,
                "volume_24h": 429690234,
                "percent_change_1h": 3463463,
                "percent_change_24h": 345634634,
                "percent_change_7d": 2902903,
                "market_cap": 23523903295092,
                "last_updated": datetime,
                "circ_supply": 235235235235,
                "total_supply": 236523532,
                "num_market_pairs": 23523
            }
        },
        ...
        { more coin objects }
    }
"""


class APICoinData:

    def __init__(self):
        # CONSTANT VARIABLES
        self.CMC_API_KEY = '6d7f5365-d3c4-4210-804e-c3c36302499d'
        self.cmc = c.CoinMarketCapAPI(self.CMC_API_KEY, sandbox=False)
        self.CC_API_KEY = '08c8a1a961728e46ff8c5b9be62d19193cbe3cdaf735150358b59778bee2294a'

        self.farming_keywords = ["pow", "mineable", "pos", "dpos", "poa"]

        # NON CONSTANT VARIABLES
        self.API_data_cmc = {
            "latest_listings": self.cmc.cryptocurrency_listings_latest()
        }
        self.names = {}
        self.symbols = {}
        self.farming_types = {}
        self.data = {}

    # PUBLIC
    def generate_static(self):
        coin_data_static = {}
        for coin in self.API_data_cmc["latest_listings"]:
            coin_obj = {
                "name": coin["name"],
                "symbol": coin["symbol"],
                "logo": "FILL OUT LATER",
                "date_added": coin["date_added"],
                "farm_type": self.get_farming_type(coin["tags"]),
            }

            coin_data_static[coin["id"]] = coin_obj
        return coin_data_static

    def generate_dynamic(self):
        coin_data_dynamic = {}
        for coin in self.API_data_cmc["latest_listings"]:
            coin_obj = {
                "price": coin["quote"]["USD"]["price"],
                "volume_24h": coin["quote"]["USD"]["volume_24h"],
                "percent_change_1h": coin["quote"]["USD"]["percent_change_1h"],
                "percent_change_24h": coin["quote"]["USD"]["percent_change_24h"],
                "percent_change_7d": coin["quote"]["USD"]["percent_change_7d"],
                "market_cap": coin["quote"]["USD"]["market_cap"],
                "last_updated": coin["last_updated"],
                "circ_supply": coin["circulating_supply"],
                "total_supply": coin["total_supply"],
                "num_market_pairs": coin["num_market_pairs"],
                "max_supply": coin["max_supply"]
            }

            coin_data_dynamic[coin["id"]] = coin_obj
        return coin_data_dynamic

    # PRIVATE
    def get_farming_type(self, tags):
        """
        Accepts list extracted from API. (see generate_static)

        RETURN KEY:
        0: PoW
        1: PoS
        2: dPoS
        3: PoA
        """
        for tag in tags:
            if tag.lower() not in self.farming_keywords:
                return "None"
            else:
                if tag.lower() == "pow" or tag.lower == "mineable":
                    return 0
                elif tag.lower() == "pos":
                    return 1
                elif tag.lower() == "dpos":
                    return 2
                elif tag.lower() == "poa":
                    return 3
