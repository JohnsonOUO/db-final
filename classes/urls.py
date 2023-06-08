from django.urls import path
from . import views

urlpatterns = [
    # path('classes/', views.stock_industry, name='classes'),
    path('classes/<str:name>', views.stock_industry_search, name='add'),
]