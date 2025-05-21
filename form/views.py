from django.http import HttpResponse
from django.shortcuts import render

from form.models import Product


# Create your views here.
def main_view(request):
    return render(request,'form.html')

def add_product_view(request):
    data=request.POST
    name=data['name']
    price=data['price']
    Product.objects.create(name=name,price=price)
    return HttpResponse(f'Product succesfully added to database')
