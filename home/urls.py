from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    #path('/stockInfo/', views.search, name='stockInfo'),
    #path('home/stockInfo/<str:num>', views.stockInfo, name='stockInfo'),
    path('home/delete/<int:stock_id>', views.delete, name='delete'),
    path('home/add/<int:stock_id>', views.add, name='add'),
]