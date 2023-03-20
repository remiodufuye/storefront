
from django.shortcuts import render
from django.db.models import Value 
from django.db.models.functions import Concat  
from store.models import Product 


def say_hello(request):

    queryset = Product.objects.filter(unit_price__gt=100)
    return render(request, 'hello.html', {'name': 'Rado','result':list(queryset)})

