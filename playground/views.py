from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


# def calculate():
#     x = 1
#     y = 2
#     return x


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Rado'})
