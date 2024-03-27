"""
URL configuration for salonproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# urls.py
from django.contrib import admin
from django.urls import path, include
from SalonSamochodowy import views
from .views import BookDetailView


def trigger_error(request):
    denominator = 0
    if denominator != 0:
        division_result = 1 / denominator
    else:
        division_result = 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
    path('car-list/', views.car_list, name='car_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]

