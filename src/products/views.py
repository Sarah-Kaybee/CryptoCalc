from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# def home_view(request, *args, **kwargs):
#     print("ARGS = ", args, "KWARGS = ", kwargs)
#     print("REQUEST = ", request)
#     print("request.user = ", request.user)
#     my_context = {}
#     return render(request, "home.html", my_context)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def calc_view(request, *args, **kwargs):
    return render(request, "<h1>Social Page</h1>")


from.models import Product
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'des': obj.description
    }
    return render(request, "products/detail.html", context)