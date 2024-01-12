from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    try:
        queryset = Product.objects.filter(unit_price__gt=20)
    except ObjectDoesNotExist:
        return render(request, 'hello.html', {'name': 'Tolga'})
    return render(request, 'hello.html', {'name': 'Tolga', 'products': list(queryset)})
