from django.shortcuts import render
from django.db.models import Value , F
from store.models import Customer 


def say_hello(request):
    queryset = Customer.objects.annotate(new_id=F('id') + 1 )
    return render(request, 'hello.html', {'name': 'Rado','result':list(queryset)})

