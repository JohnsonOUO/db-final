from django.urls import path
from . import views

urlpatterns = [
    #path('home/', views.home, name='home'),
    path('Search/', views.search, name='search'),
    path('stockInfo/<str:num>', views.stockInfo, name='stockInfo'),
    #path('index/', views.index, name='index'),
]