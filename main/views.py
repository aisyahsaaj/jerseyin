from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()
    context = {
        'npm' : '2406435585',
        'name': 'Aisyah Saajidah',
        'class': 'PBP D'
    }
    return render(request, 'main.html', context)