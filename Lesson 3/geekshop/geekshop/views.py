from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def main(request):
    products = Product.objects.all()[:4]

    context = {
        'description': 'Офигенские СТУЛЬЯ',
        'subject': 'Популярно в лучших домах Филадельфии',
        'products': products
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    return render(request, 'contact.html')