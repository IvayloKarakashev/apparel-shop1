from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.web.forms import ProductAddForm
from firstProject.web.models import Product, Category


class CategoriesView(generic_views.ListView):
    model = Category
    template_name = 'front-end/categories.html'


class ProductDetailsView(generic_views.DetailView):
    model = Product
    template_name = 'front-end/product-details.html'


class ProductsView(generic_views.ListView):
    model = Product
    template_name = 'front-end/products.html'

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['pk'])


def is_seller(user):
    return user.groups.filter(name='Sellers').exists()


class ProductAddView(UserPassesTestMixin, generic_views.CreateView):
    model = Product
    template_name = 'front-end/product-add.html'
    form_class = ProductAddForm

    def test_func(self):
        return is_seller(self.request.user)

    def form_valid(self, form):
        print(self.request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.uploaded_by = self.request.user
            obj.save()

            return redirect(reverse_lazy('index'))