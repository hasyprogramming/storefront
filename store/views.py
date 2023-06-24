from django.shortcuts import render
from store.models import Customer, Collection, Products, Order, OrderItem

def practice(request):
    order = Order.objects.all()[-5:]