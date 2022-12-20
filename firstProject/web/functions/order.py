import json

from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from firstProject.web.models import Product, ProductSize, Order, OrderItem


def get_or_create_order_item(customer, product_id, product_size):
    product = Product.objects.get(id=product_id)
    size = ProductSize.objects.get(product=product, name=product_size)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product, size=size)

    return order_item


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data['productId']
    product_size = data['size']
    quantity = data['quantity']

    order_item = get_or_create_order_item(customer=request.user, product_id=product_id, product_size=product_size)
    order_item.quantity += int(quantity)
    order_item.save()


def update_item_quantity(request):
    data = json.loads(request.body)
    product_id = data['productId']
    product_size = data['size']
    action = data['action']

    order_item = get_or_create_order_item(customer=request.user, product_id=product_id, product_size=product_size)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'subtract':
        order_item.quantity -= 1

    order_item.save()

    if action == 'remove' or order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added.', safe=False)
