from django.shortcuts import render
from django.shortcuts import render

# SOURCES:
# https://colorswall.com/images/palettes/ethereum-web-design-isometric-colors-palette-6108-colorswall.png
# https://colorswall.com/images/palettes/crypto-dashboard-color-palette-1182-colorswall.png
eth_color_palette = {
    "light_blue": "#48cbd9",
    "baby_blue": "#79e7e7",
    "dark_blue": "#14044d",
    "blue_grey": "#716b94",
    "white_grey": "#c6c5d4",
    "deep_blue": "#37367b",
    "pale_purple": "d37fcc"
}

# SOURCES:
# https://convertingcolors.com/color-palette-image/view/F2A900D38F00B47500965D007845005B2F00401A00270200000000.png
btc_orange_palette = {
    "light_yellow": "#F2A900",
    "light_gold": "#D38F00",
    "medium_gold": "#B47500",
    "dark_gold": "#965D00",
    "light_brown": "#784500",
    "medium_brown": "#5B2F00",
    "dark_brown": "#401A00",
    "blackish_brown": "#270200",
}


def join_palettes(palettes):
    joined = {}
    if len(palettes) == 0:
        return None
    elif len(palettes) == 1:
        return palettes[1]
    else:
        for p in palettes:
            joined.update(p)


def home_view(request, *args, **kwargs):
    print("ARGS = ", args, "KWARGS = ", kwargs)
    print("REQUEST = ", request)
    print("request.user = ", request.user)
    my_context = {
        "coin_list": ["BTC", "ETH", "LINK", "DOT"],
        "colors": join_palettes([btc_orange_palette, eth_color_palette]),
        "chosen_coin": "Polkadot",
        "coin_type": "Staking"
    }
    return render(request, "home.html", my_context)
