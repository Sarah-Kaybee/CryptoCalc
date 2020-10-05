from cryptocompy import coin, price, mining, top

coin_list = coin.get_coin_list(coins="all")
print(len(coin_list))

for c in coin_list:
    print(c)

symbols = list(coin_list.keys())
print("symbols = ", symbols)
