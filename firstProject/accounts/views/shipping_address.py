import json

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views
from firstProject.accounts.models import Profile
from firstProject.web.forms import ShippingAddressForm
from firstProject.web.models import Order, ShippingAddress


class ShippingAddressView(generic_views.CreateView):
    form_class = ShippingAddressForm
    template_name = 'front-end/checkout.html'


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


def select_address(request):
    page_title = 'Select Address'
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
        'addresses': shipping_addresses,
        'page_title': page_title
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
    page_title = 'Enter address'
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
        'form': form,
        'page_title': page_title
    }

    return render(request, 'front-end/enter-new-address.html', context)
