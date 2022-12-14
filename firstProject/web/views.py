import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views, generic as generic_views

from firstProject.accounts.models import Profile
from firstProject.web.forms import ShippingAddressForm
from firstProject.web.models import Product, Category, OrderItem, Order, ShippingAddress, WishList, FAQ, ProductSize


def home_view(request, profile=None):
    categories = Category.objects.all()
    if request.user.is_authenticated and not request.user.is_superuser:
        profile = Profile.objects.get(user_id=request.user.id)

    context = {
        'categories': categories,
        'pofile': profile
    }
    return render(request, 'index.html', context)


class CustomDetailView(views.DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context


class ProductDetailsView(CustomDetailView):
    model = Product
    template_name = 'front-end/product-details.html'


class CategoriesView(views.ListView):
    model = Category
    template_name = 'front-end/categories.html'


class ProductsView(views.ListView):
    model = Product
    template_name = 'front-end/products.html'

    def get_queryset(self):
        # print(dir(self))
        # print(self.args)
        # print(self.kwargs)
        # print(self.request)
        return Product.objects.filter(category=self.kwargs['pk'])


class WishListView(views.ListView):
    model = WishList
    template_name = 'front-end/wishlist.html'

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)


def cart(request):
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
        'categories': categories
    }

    return render(request, 'front-end/cart.html', context)


def clear_items(request):
    customer = request.user
    order_items = Order.objects.get(customer=customer, complete=False).orderitem_set.all()
    order_items.delete()

    return redirect(reverse_lazy('cart'))


def select_address(request):
    if request.user.is_authenticated:
        customer = request.user
        profile = Profile.objects.get(user_id=customer.id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        shipping_addresses = ShippingAddress.objects.filter(profile_id=profile.pk)

    context = {
        'items': items,
        'order': order,
        'profile': profile,
        'addresses': shipping_addresses
    }

    if request.method == 'GET':
        if shipping_addresses:
            return render(request, 'front-end/select-address.html', context)
        return redirect(reverse_lazy('enter new address'))

    if request.method == 'POST':
        data = json.loads(request.body)
        selected_address_id = data['addressId']
        order.shipping_address = ShippingAddress.objects.get(id=selected_address_id)
        order.save()

        return redirect(reverse_lazy('checkout'))


def enter_new_address(request):
    form = ShippingAddressForm()

    if request.user.is_authenticated:
        customer = request.user
        profile = Profile.objects.get(user_id=customer.id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

        if request.method == 'GET':
            form = ShippingAddressForm()

        if request.method == 'POST':

            form = ShippingAddressForm(request.POST)

            if form.is_valid():
                address = form.save(commit=False)
                address.profile = profile
                address.save()

                order.shipping_address = address
                order.save()

            return redirect(reverse_lazy('checkout'))

    context = {
        'customer': customer,
        'profile': profile,
        'order': order,
        'items': items,
        'form': form
    }

    return render(request, 'front-end/enter-new-address.html', context)


def checkout(request):
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
        'address': shipping_address
    }

    return render(request, 'front-end/checkout.html', context)


def finalize_order(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        order.complete = True
        order.save()

        return redirect(reverse_lazy('order success', kwargs={'pk': order}))


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


def update_wishlist(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    user = request.user
    product = Product.objects.get(id=product_id)
    item, created = WishList.objects.get_or_create(user=user, product=product)
    if action == 'remove':
        item.delete()

    return JsonResponse('Wishlist was updated.', safe=False)


class ShippingAddressView(views.CreateView):
    form_class = ShippingAddressForm
    template_name = 'front-end/checkout.html'


# def form_valid(self, form):
#     shipping_address = form.save(commit=False)
#     print(shipping_address)
#     shipping_address.profile_id =


class OrderSuccessView(views.DetailView):
    model = Order
    template_name = 'front-end/order-success.html'

    def get_queryset(self):
        return Order.objects.filter(pk=self.kwargs['pk'])


class OrderTrackingView(views.DetailView):
    model = Order
    template_name = 'front-end/order-tracking.html'

    def get_queryset(self):
        return Order.objects.filter(pk=self.kwargs['pk'])


class UserAddressesView(generic_views.ListView):
    model = ShippingAddress
    template_name = 'front-end/user-addresses.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(profile=self.kwargs['pk'])


class AddUserAddressView(generic_views.CreateView):
    form_class = ShippingAddressForm
    template_name = 'front-end/user-shipping-address-add.html'

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.profile = Profile.objects.get(user_id=self.request.user)
            obj.save()

            return redirect(reverse_lazy('user shipping addresses', kwargs={'pk': obj.profile.pk}))


class EditUserShippingAddressView(generic_views.UpdateView):
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'front-end/user-shipping-address-edit.html'

    def get_success_url(self):
        return reverse_lazy('user shipping addresses', kwargs={'pk': self.object.profile_id})


class DeleteUserShippingAddressView(generic_views.DeleteView):
    model = ShippingAddress
    template_name = 'front-end/user-shipping-address-confirm-delete.html'

    def get_success_url(self):
        return reverse_lazy('user shipping addresses', kwargs={'pk': self.object.profile_id})


class FAQView(generic_views.ListView):
    model = FAQ
    template_name = 'front-end/faq.html'


class TermsAndConditionsView(generic_views.TemplateView):
    template_name = 'front-end/terms.html'


class AboutView(generic_views.TemplateView):
    template_name = 'front-end/about-us.html'


class TestView(generic_views.TemplateView):
    template_name = 'front-end/shop-filter-hide.html'


class TestView2(generic_views.TemplateView):
    pass
