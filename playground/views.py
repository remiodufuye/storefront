from django.shortcuts import render
from django.db.models import Count ,Min
from store.models import Product ,Order


def say_hello(request):
    result = Order.objects.aggregate(count =Count('id'))
    return render(request, 'hello.html', {'name': 'Rado','result':result})

