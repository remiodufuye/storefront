
from django.shortcuts import render
from django.db import transaction
from store.models import Collection ,Order, OrderItem


def say_hello(request):
    
    return render(request, 'hello.html', {'name': 'Rado'}) 

