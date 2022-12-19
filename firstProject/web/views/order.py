import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.accounts.models import Profile
from firstProject.utilities.mixins import PageTitleMixin
from firstProject.web.models import Order, Category, Product, ProductSize, OrderItem, ShippingAddress


@login_required
def cart(request):
    page_title = 'Cart'

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        categories = Category.objects.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order': order,
        'categories': categories,
        'page_title': page_title
    }

    return render(request, 'front-end/cart.html', context)


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data['productId']
    product_size = data['size']
    quantity = data['quantity']

    customer = request.user
    product = Product.objects.get(id=product_id)
    size = ProductSize.objects.get(product=product, name=product_size)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product, size=size)
    print(quantity)
    order_item.quantity += int(quantity)
    order_item.save()


def update_item_quantity(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    product_size = data['size']

    customer = request.user
    product = Product.objects.get(id=product_id)
    size = ProductSize.objects.get(product=product, name=product_size)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product, size=size)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'subtract':
        order_item.quantity -= 1

    order_item.save()

    if action == 'remove' or order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added.', safe=False)


def clear_items(request):
    customer = request.user
    order_items = Order.objects.get(customer=customer, complete=False).orderitem_set.all()
    order_items.delete()

    return redirect(reverse_lazy('cart'))


def checkout(request):
    page_title = 'Checkout'

    if request.user.is_authenticated:
        customer = request.user
        profile = Profile.objects.get(user_id=customer.id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        shipping_address = ShippingAddress.objects.get(id=order.shipping_address.id)

        # return redirect(reverse_lazy('order success', kwargs={'pk': order}))

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order': order,
        'profile': profile,
        'address': shipping_address,
        'page_title': page_title
    }

    return render(request, 'front-end/checkout.html', context)


def finalize_order(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        order.complete = True
        order.save()

        return redirect(reverse_lazy('order success', kwargs={'pk': order}))


class OrderSuccessView(PageTitleMixin, generic_views.DetailView):
    page_title = 'Order completed'
    model = Order
    template_name = 'front-end/order-success.html'

    def get_queryset(self):
        return Order.objects.filter(pk=self.kwargs['pk'])


class OrderTrackingView(PageTitleMixin, generic_views.DetailView):
    page_title = 'Track order'
    model = Order
    template_name = 'front-end/order-tracking.html'

    def get_queryset(self):
        return Order.objects.filter(pk=self.kwargs['pk'])
