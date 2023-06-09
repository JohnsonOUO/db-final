from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.routehome, name='routehome'),
    #path('/stockInfo/', views.search, name='stockInfo'),
    #path('home/stockInfo/<str:num>', views.stockInfo, name='stockInfo'),
    path('home/delete/<int:stock_id>', views.delete, name='delete'),
    path('home/add/<int:stock_id>', views.add, name='add'),
    path('home/<str:stock_classname>', views.favor_class, name='favor_class'),
]