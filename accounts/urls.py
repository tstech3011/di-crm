from django.urls import path
from . import views
from .views import ProductListView

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    # path('products/', views.products, name='products'),
    path('products/', ProductListView.as_view(), name='products'),
    path('customer/', views.customer, name='customer'),
]