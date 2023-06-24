from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg
from django.http import HttpResponse
from store.models import Order, Product
def say_hello(request):
    result = Order.objects.aggregate(count=Count('id'))
    result = Order.objects.filter(customer_id=1).aggregate(count=Count('id'))
    return render(request, 'hello.html', {'name': 'Mosh', 'result': result})
