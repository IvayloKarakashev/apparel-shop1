import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views, generic as generic_views

from firstProject.accounts.models import Profile
from firstProject.web.forms import ShippingAddressForm
from firstProject.web.models import Product, Category, OrderItem, Order, ShippingAddress


class HomeView(views.TemplateView):
    template_name = 'index.html'


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'front-end/product-details.html'


class CategoriesView(views.ListView):
    model = Category
    template_name = 'front-end/categories.html'

    # def get_queryset(self):
    #     return Category.objects.all()


class ProductsView(views.ListView):
    model = Product
    template_name = 'front-end/products.html'

    def get_queryset(self):
        # print(dir(self))
        # print(self.args)
        # print(self.kwargs)
        # print(self.request)
        return Product.objects.filter(category=self.kwargs['pk'])


# def add_to_cart(request, product_id):
#     item = get_object_or_404(Product, id=product_id)
#     order_item = OrderItem.objects.create(item=item)
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.items.filter(item_id=item.id).exists():
#             order_item.quantity += 1
#             order_item.save()
#         else:
#             pass
#     else:
#         order = Order.objects.create(user=request.user)
#         order.items.add(order_item)
#     return redirect('home', pk=product_id)

def cart(request):
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
    }

    return render(request, 'front-end/cart.html', context)


def checkout(request):
    form = ShippingAddressForm()

    if request.user.is_authenticated:
        customer = request.user
        profile = Profile.objects.get(user_id=customer.id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        shipping_addresses = ShippingAddress.objects.filter(profile_id=profile.pk)

        if request.method == 'GET':
            form = ShippingAddressForm()

        if request.method == 'POST':
            form = ShippingAddressForm(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.customer = customer  # Do I need it here ?
                obj.profile = profile
                obj.order = order

                obj.save()

                return redirect(reverse_lazy('order success', kwargs={'pk': order}))

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order': order,
        'form': form,
        'profile': profile,
        'addresses': shipping_addresses
    }

    return render(request, 'front-end/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    print(data)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('ProductId', productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added.', safe=False)


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
