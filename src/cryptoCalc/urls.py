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
import ops.api_requests_cmc as api
from calculator import views as calc_views

urlpatterns = [
    # API
    # path('', api.latest_listings, 'api-data'),

    # VIEWS
    path('', calc_views.home_view, name='home'),
    path('api-data/', calc_views.get_data, name='api-data'),
    path('home/', calc_views.home_view, name='home'),
    path('coin_stats/', calc_views.coin_stats_view, name='coin_stats'),
    path('contact/', calc_views.contact_view, name='contact'),
    path('about/', calc_views.about_view, name="about"),
    path('admin/', admin.site.urls),
]

