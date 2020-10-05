from django.shortcuts import render
from django.http import JsonResponse
from ops import api_requests_cmc as api
import threading
import time

run_status = True


# globals
data = {}               # updated every 5 minutes (raw API data)
coin_static = {}        # updated every 5 minutes
coin_dynamic = {}       # updated every 1 day


coin_data = {
    coin_static,
    coin_dynamic
}


def update_data():
    i = 0
    while i == 0:
        data = api.APICoinData()
        time.sleep(300)


def update_dynamic(data):
    """
    Infinite loop.
    Updates variables every 5:01 minutes whilst the server is running.
    5:01 for safe room if update_data is slow.
    """
    i = 0
    while i == 0:
        coin_dynamic = data.generate_dynamic()
        time.sleep(300)


def update_static(data):
    """
    Infinite loop
    Updates variables every 1 day whilst the server is running.
    """
    i = 0
    while i == 0:
        coin_static = data.generate_static()
        time.sleep(86400)


update_data_thread = threading.Thread(target=update_data)
update_data_thread.start()

update_dynamic_thread = threading.Thread(target=update_dynamic)
update_dynamic_thread.start()



def home_view(request, coin_data, *args, **kwargs):
    print("ARGS = ", args, "KWARGS = ", kwargs)
    print("REQUEST = ", request)
    print("request.user = ", request.user)
    my_context = {
        "coin_list": ["BTC", "ETH", "LINK", "DOT"],
        "chosen_coin": "DOT",
        "coin_type": "Staking"
    }
    return render(request, "home.html", my_context)


def coin_stats_view(request, coin_data, *args, **kwargs):
    return render(request, "coin_stats.html", {})


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