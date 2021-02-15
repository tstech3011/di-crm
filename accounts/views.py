from django.shortcuts import render
from django.views.generic import ListView
from .models import *


def home(request):
  orders = Order.objects.all()
  customers = Customer.objects.all()

  total_customers = customers.count()
  total_orders = orders.count()

  orders_pending = Order.objects.filter(status='Pending').count()
  orders_delivered = Order.objects.filter(status='Delivered').count()


  context = {
            'orders': orders,
            'customers': customers,
            'total_orders' : total_orders,
            'orders_pending' : orders_pending,
            'orders_delivered' : orders_delivered,
            }
  return render(request, 'accounts/dashboard.html', context)
  
# def products(request):
#   product_list = Product.objects.all()
#   context = {
#       'product_list': product_list,
#       'title' : 'Products'

#   }
#   return render(request, 'accounts/products.html', context)

class ProductListView(ListView):
  model = Product
  template_name = 'accounts/products.html'
  context_object_name = 'product_list'

  # def title(self):
  #   context = {'title' : 'Products'}
  #   return context

  
def customer(request):
  return render(request, 'accounts/customer.html', {'title' : 'Customer'})
  
def contact(request):
  return render(request, 'accounts/contact.html', {'title' : 'Contact'})
  
