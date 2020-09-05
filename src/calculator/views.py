from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print("ARGS = ", args, "KWARGS = ", kwargs)
    print("REQUEST = ", request)
    print("request.user = ", request.user)
    my_context = {
        "coin_list": ["BTC", "ETH", "LINK", "DOT"],
        "chosen_coin": "DOT",
        "coin_type": "Staking"
    }
    return render(request, "home.html", my_context)
