import tempfile

from datetime import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.api.gcs import upload_blob
from firstProject.web.forms import ProductAddForm, ProductEditForm
from firstProject.web.functions.products import is_seller
from firstProject.web.models import Product, Category


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


class SellerProductsView(UserPassesTestMixin, generic_views.ListView):
    model = Product
    template_name = 'front-end/products.html'

    def test_func(self):
        print(f"Is seller:{is_seller(self.request.user)}")
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
        if form.is_valid():
            obj = form.save(commit=False)
            obj.uploaded_by = self.request.user

            image_file = self.request.FILES['image']
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_blob_name = f"user-uploaded-images_apparelshop1/{timestamp}_{image_file.name}"
            upload_blob('user-uploaded-images_apparelshop1', image_file, image_blob_name)

            obj.image.name = image_blob_name
            obj.save()

            return redirect(reverse_lazy('index'))


class ProductEditView(UserPassesTestMixin, generic_views.UpdateView):
    model = Product
    template_name = 'front-end/product-edit.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('seller products')

    def test_func(self):
        return is_seller(self.request.user)

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)

            # Check if a new image has been uploaded
            if 'image' in self.request.FILES:
                # Upload the new image to Google Cloud Storage
                image_file = self.request.FILES['image']
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                image_blob_name = f"user-uploaded-images_apparelshop1/{timestamp}_{image_file.name}"
                upload_blob('user-uploaded-images_apparelshop1', image_file, image_blob_name)
                obj.image.name = image_blob_name

            obj.save()
            return redirect(self.success_url)

