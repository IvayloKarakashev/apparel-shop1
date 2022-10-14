from django.shortcuts import render
from django.views import generic as views

from firstProject.web.models import Product, Category


class HomeView(views.TemplateView):
    template_name = 'web/index.html'


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'web/product_details.html'


class CategoriesView(views.ListView):
    model = Category
    template_name = 'web/categories.html'


class SingleCategoryView(views.ListView):
    model = Product
    template_name = 'web/single_category.html'

    def get_queryset(self):
        # print(dir(self))
        # print(self.args)
        # print(self.kwargs)
        # print(self.request)
        return Product.objects.filter(category=self.kwargs['pk'])
