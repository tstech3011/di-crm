from django.shortcuts import render


def home(request):
  return render(request, 'accounts/dashboard.html', {'title' : 'Dashboard'})
  
def products(request):
  return render(request, 'accounts/products.html', {'title' : 'Products'})
  
def customer(request):
  return render(request, 'accounts/customer.html', {'title' : 'Customer'})
  
def contact(request):
  return render(request, 'accounts/contact.html', {'title' : 'Contact'})
  
