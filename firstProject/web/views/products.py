from django.views import generic as generic_views
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
