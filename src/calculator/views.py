from django.shortcuts import render
from django.http import JsonResponse


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


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def get_data(request, *args, **kwargs):
    data = {
        "coin": None,
        "id": 1,
        "info": {"one": 1, "two": 2}
    }
    return JsonResponse(data)