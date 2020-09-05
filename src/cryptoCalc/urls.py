"""cryptoCalc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from products import views as product_views
from calculator import views as calc_views

urlpatterns = [
    path('', calc_views.home_view, name='home'),
    path('home/', calc_views.home_view, name='home'),
    path('contact/', product_views.contact_view, name='contact'),
    path('about/', product_views.about_view, name="about"),
    path('admin/', admin.site.urls),
    path('products/', product_views.product_detail_view)
]

