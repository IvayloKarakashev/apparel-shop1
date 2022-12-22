from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.web.forms import ProductAddForm, ProductEditForm
from firstProject.web.functions.products import is_seller
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


class SellerProductsView(UserPassesTestMixin, generic_views.ListView):
    model = Product
    template_name = 'front-end/products.html'

    def test_func(self):
        return is_seller(self.request.user)

    def get_queryset(self):
        return Product.objects.filter(uploaded_by=self.request.user.id)


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


class ProductEditView(UserPassesTestMixin, generic_views.UpdateView):
    model = Product
    template_name = 'front-end/product-edit.html'
    form_class = ProductEditForm

    success_url = reverse_lazy('seller products')

    def test_func(self):
        return is_seller(self.request.user)
