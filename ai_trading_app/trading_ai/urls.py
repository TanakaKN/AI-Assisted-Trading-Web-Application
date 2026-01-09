from django.urls import path
from .views import home, analyze_stock

urlpatterns = [
    path("", home, name="home"),
    path("analyze/", analyze_stock, name="analyze_stock"),
]
