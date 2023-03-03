from django.shortcuts import render
# from django.db.models import Q,F
from store.models import Product ,Order


def say_hello(request):
    queryset = Order.objects.select_related('customer').order_by('-placed_at')[:5]
    return render(request, 'hello.html', {'name': 'Rado','orders':list(queryset)})

