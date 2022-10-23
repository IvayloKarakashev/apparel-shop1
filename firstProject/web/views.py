from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from firstProject.web.models import Product, Category, OrderItem, Order


class HomeView(views.TemplateView):
    template_name = 'web/home-page.html'


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'web/product-page.html'


class CategoriesView(views.ListView):
    model = Category
    template_name = 'web/categories.html'

    # def get_queryset(self):
    #     return Category.objects.all()


class SingleCategoryView(views.ListView):
    model = Product
    template_name = 'web/single_category.html'

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

    return render(request, 'web/cart.html', context)
