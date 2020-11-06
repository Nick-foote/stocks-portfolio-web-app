from django.urls import path
from . import views
from .dash_apps.finished_apps import stock_graphic      # Required to preload here

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stocks/', views.stocks, name='stocks'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete/<symbol>', views.delete, name='delete'),
]
