from django.urls import path

from firstProject.web.views import HomeView, CategoriesView, ProductsView, ProductDetailsView, cart, update_item, \
    checkout, OrderSuccessView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>', ProductsView.as_view(), name='products'),
    path('products/details/<int:pk>', ProductDetailsView.as_view(), name='product details'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', update_item, name='update item'),
    path('order-success/<int:pk>', OrderSuccessView.as_view(), name='order success'),
    # path('test/', ShippingAddressView.as_view(), name='test view')
)
