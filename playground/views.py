from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product
from store.models import OrderItem


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    queryset = Product.objects.filter(id__in=OrderItem.objects.values_list('product_id').distinct()).order_by('title')
    return render(request, 'hello.html', {'name': 'Tolga', 'products': list(queryset)})
#OrderItem.objects.values('product_id')