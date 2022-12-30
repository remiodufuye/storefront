from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Views In Django Are More of a request handler , like controllers in Ruby 
# request - > response


def say_hello(request):
    return HttpResponse('Hello From Django!!!')