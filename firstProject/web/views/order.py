from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.accounts.models import Profile
from firstProject.utilities.mixins import PageTitleMixin
from firstProject.web.models import Order, Category, Product, ProductSize, OrderItem, ShippingAddress


def cart_view(request):
    page_title = 'Cart'

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order': order,
        'page_title': page_title
    }

    return render(request, 'front-end/cart.html', context)


@login_required()
def checkout_view(request):
    try:
        page_title = 'Checkout'

        customer = request.user
        profile = Profile.objects.get(user_id=customer.id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        shipping_address = ShippingAddress.objects.get(id=order.shipping_address.id)

        context = {
            'items': items,
            'order': order,
            'profile': profile,
            'address': shipping_address,
            'page_title': page_title
        }

        return render(request, 'front-end/checkout.html', context)

    except AttributeError:
        return redirect(reverse_lazy('cart'))


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


def clear_items(request):
    customer = request.user
    order_items = Order.objects.get(customer=customer, complete=False).orderitem_set.all()
    order_items.delete()

    return redirect(reverse_lazy('cart'))


def finalize_order(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        order.complete = True
        order.save()

        return redirect(reverse_lazy('order success', kwargs={'pk': order}))
