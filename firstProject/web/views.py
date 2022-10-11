from django.shortcuts import render
from django.views import generic as views

from firstProject.web.models import Product, Category


class HomeView(views.TemplateView):
    template_name = 'web/index.html'


# class ProductsView(views.ListView):
#     model = Product
#     template_name = 'web/products.html'


# class ProductDetailsView(views.DetailView):
#     model = Product
#     template_name = 'web/product_details.html'
#     context_object_name = 'product'


class CategoriesView(views.ListView):
    model = Category
    template_name = 'web/categories.html'


class SingleCategoryView(views.ListView):
    model = Category
    template_name = 'web/single_category.html'
    context_object_name = 'category'
