from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    #path('/stockInfo/', views.search, name='stockInfo'),
    #path('home/stockInfo/<str:num>', views.stockInfo, name='stockInfo'),
    path('home/delete/<int:id>', views.delete, name='delete'),
    path('home/add/<int:id>', views.add, name='add'),
]