from cryptocompy import coin, price
import coinmarketcapapi as cmc      # only used to extract fiat data

"""
        Private variables denoted by ___variable.
        Double-private variables denoted by ___variable___
"""


class APICoinData:
    def __init__(self, cmc_api_key='6d7f5365-d3c4-4210-804e-c3c36302499d'):
        self.___CMC_API_KEY = cmc_api_key
        self.___cmc = cmc.CoinMarketCapAPI(self.___CMC_API_KEY, sandbox=False)

        # THIS API CALL COSTS CREDITS
        # self.___fiat_data = self.___cmc.fiat_map().data

        self.coin_list = coin.get_coin_list(coins='all')
        self.___coin_symbols___ = list(self.coin_list.keys())
        # self.___fiat_symbols___ = [fiat["symbol"] for fiat in self.___fiat_data]
        # self.___price_list = price.get_current_price(self.___coin_symbols___, self.___fiat_symbols___, e='all', try_conversion=True, full=True, format='raw')

        # self.mining_equipment = mining.get_mining_equipment()
        # self.mining_contracts = mining.get_mining_contracts()

        # Putting all variables into one dict for when we need to draw from multiple dictionaries.

    def generate_static(self):
        coin_data_static = {}
        for symbol, coin_data in self.coin_list:
            if symbol != coin_data["Name"]:
                print("APICoinData.generate_static() ERROR: key != data['Name'] for ", symbol)
            coin_obj = {
                "name": coin_data["CoinName"],
                "symbol": coin_data["Name"],
                "logo": coin_data["ImageUrl"],
                "farm_type": coin_data["ProofType"]
            }

            coin_data_static[symbol] = coin_obj
        return coin_data_static

    def generate_dynamic(self):
        coin_data_dynamic = {}
        for coin_data in self.coin_list:
            coin_obj = {
                "price_data": {
                    "prices": [],
                    "volume_24h": [],
                    "percent_change_1h": [],
                    "percent_change_24h": [],
                    "percent_change_7d": [],
                    "market_cap": []
                },
                "supply_data": {
                    "circ_supply": [],
                    "total_supply": [],
                    "num_market_pairs": [],
                    "max_supply": []
                }
            }

            coin_data_dynamic[coin_data["Id"]] = coin_obj
        return coin_data_dynamic


data = APICoinData()
proof_types = {}
print(data.coin_list)
print(type(data.coin_list))
for coin in data.coin_list:
    print(data.coin_list[coin])
    if data.coin_list[coin]["ProofType"] not in proof_types:
        proof_types[data.coin_list[coin]["ProofType"]] = 1
    else:
        proof_types[data.coin_list[coin]["ProofType"]] += 1

print(proof_types)
print(len(proof_types))

# proof types: { 'PoW/PoS': 597, 'PoS': 344, 'PoW': 653, 'N/A': 3560, 'PoS/PoW/PoT': 1, 'PoST': 1, 'PoB/PoS': 1,
# 'DPoR': 1, 'PoW/PoM/PoSII': 1, 'PoS/PoB': 1, 'PoP/PoV/PoQ': 1, 'PoB': 1, 'PoA': 6, 'PoW/HiPoS': 1, 'PoW/PoS/PoC': 1,
# 'PoS/PoW': 8, 'Proof of Trust': 1, 'Pow/PoSC': 1, 'DPoS': 41, 'PoS/PoP': 1, 'DPoS/LPoS': 4, 'PoWT': 1, 'PoW/PoW': 1,
# 'PoS ': 1, 'TPoS': 1, 'PoP': 2, 'PoW/PoS ': 3, ' PoW/PoS': 1, 'mFBA': 1, 'PoPP': 1, 'Proof of Ownership': 1,
# 'PoW/DPoW': 1, '240000000': 1, 'Proof of Stake': 1, 'Scrypt-adaptive-N (ASIC resistant)': 1, 'PoS/PoD': 1, 'POBh': 1,
# 'PoW + Hive': 1, 'DPoW': 1, 'Pos': 2, 'DPoC': 1, 'POS / MN': 1, 'Consortium': 1, 'LPoS': 2, 'PoP + PoW': 1,
# 'DPoI': 1, 'Proof of Authority': 2, 'PoC': 4, 'PoW/PoZ': 1, 'fPoW+ PBFT': 1, 'dPoS': 1, 'PoWPoS': 1, 'PoR': 1,
# 'Limited Confidence Proof-of-Activity ': 1, 'HPoW': 1, 'SPoS': 1, 'PoS/PoM': 1, 'ePoW': 1, 'Zero-Knowledge Proof': 1,
# 'DPOS': 1, 'PoSign': 1, ' PoW/PoS/PoA': 1, 'dPoS/BFT': 1, 'PoW+PoS': 1, 'PoS/LPoS': 1, 'PoW/nPoS': 1, 'Tangle': 1,
# 'PoI': 1, 'dPoW/PoW': 1}