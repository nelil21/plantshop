from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'app_name': 'PlantShop',
    }
    return render(request, 'main/index.html', context)
