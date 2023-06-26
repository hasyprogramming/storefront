from django.db import models, transaction
from django.shortcuts import render
from store.models import Product, Customer, Order, OrderItem, Product, Collection, Cart, CartItem
@transaction.atomic()
def say_hello(request):
    cart = Cart()
    cart.save()
    item1 = CartItem()
    item1.cart = cart
    item1.product_id = 1
    item1.quantity = 2
    item1.save()

    item1 = CartItem.objects.get(pk=1)
    item1.quantity = 2
    item1.save()
    return render(request, 'hello.html', {'name': 'hasy'})
