import os
import tempfile

from datetime import datetime

from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.api.gcs import upload_blob
from firstProject.settings import PRODUCTION
from firstProject.web.forms import ProductAddForm, ProductEditForm, ProductSizeFormSet
from firstProject.web.functions.products import is_seller
from firstProject.web.models import Product


class ProductDetailsView(generic_views.DetailView):
    model = Product
    template_name = 'front-end/product-details.html'


class ProductsView(generic_views.ListView):
    model = Product
    template_name = 'front-end/products.html'
    paginate_by = 15

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['pk']).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context['products'] = products
        context['get_obj'] = queryset
        return context


class SellerProductsView(UserPassesTestMixin, ProductsView):
    def test_func(self):
        return is_seller(self.request.user)

    def get_queryset(self):
        return Product.objects.filter(uploaded_by=self.request.user.id).order_by('-id')


class ProductAddView(UserPassesTestMixin, generic_views.CreateView):
    model = Product
    template_name = 'front-end/product-add.html'
    form_class = ProductAddForm
    success_url = reverse_lazy('seller products')

    def test_func(self):
        return is_seller(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['size_formset'] = ProductSizeFormSet()
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.uploaded_by = self.request.user

        if PRODUCTION:
            image_file = self.request.FILES['image']
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_blob_name = f"user-uploaded-images_apparelshop1/{timestamp}_{image_file.name}"
            upload_blob('user-uploaded-images_apparelshop1', image_file, image_blob_name)
            obj.image.name = image_blob_name

        size_formset = ProductSizeFormSet(self.request.POST, instance=obj)
        if size_formset.is_valid():
            obj.save()
            size_formset.save()

        return super().form_valid(form)


class ProductEditView(UserPassesTestMixin, generic_views.UpdateView):
    model = Product
    template_name = 'front-end/product-edit.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('seller products')

    def test_func(self):
        return is_seller(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['size_formset'] = ProductSizeFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)

        # Check if a new image has been uploaded
        if 'image' in self.request.FILES:
            # Upload the new image to Google Cloud Storage
            image_file = self.request.FILES['image']
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_blob_name = f"user-uploaded-images_apparelshop1/{timestamp}_{image_file.name}"
            upload_blob('user-uploaded-images_apparelshop1', image_file, image_blob_name)
            obj.image.name = image_blob_name

        size_formset = ProductSizeFormSet(self.request.POST, instance=obj)
        # if size_formset.is_valid():
        obj.save()
        size_formset.save()

        return super().form_valid(form)
