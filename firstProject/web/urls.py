from django.urls import path

from firstProject.accounts.views.shipping_address import select_address, enter_new_address
from firstProject.web.functions.order import update_item_quantity, add_to_cart
from firstProject.web.functions.wishlist import update_wishlist
from firstProject.web.views.generic import home_view
from firstProject.web.views.order import cart_view, checkout_view, OrderSuccessView, OrderTrackingView, finalize_order, \
    clear_items
from firstProject.web.views.products import ProductsView, ProductDetailsView, ProductAddView, \
    ProductEditView, SellerProductsView
from firstProject.web.views.static import FAQView, TermsAndConditionsView, AboutView
from firstProject.web.views.wishlist import WishListView

urlpatterns = (
    path('', home_view, name='index'),
    path('categories/<int:pk>/', ProductsView.as_view(), name='products'),
    path('products/seller-products/', SellerProductsView.as_view(), name='seller products'),
    path('products/details/<int:pk>/', ProductDetailsView.as_view(), name='product details'),
    path('products/add/', ProductAddView.as_view(), name='add product'),
    path('products/edit/<int:pk>/', ProductEditView.as_view(), name='edit product'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('cart/', cart_view, name='cart'),
    path('select-address/', select_address, name='select address'),
    path('enter-new-address/', enter_new_address, name='enter new address'),
    path('checkout/', checkout_view, name='checkout'),
    path('finalize-order/', finalize_order, name='finalize order'),
    path('update-item-quantity/', update_item_quantity, name='update item quantity'),
    path('add-to-cart/', add_to_cart, name='add to cart'),
    path('clear-items/', clear_items, name='clear items'),
    path('update-wishlist/', update_wishlist, name='update wishlist'),
    path('order-success/<int:pk>/', OrderSuccessView.as_view(), name='order success'),
    path('order-tracking/<int:pk>/', OrderTrackingView.as_view(), name='order tracking'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('terms/', TermsAndConditionsView.as_view(), name='terms and conditions'),
    path('about/', AboutView.as_view(), name='about us'),
)
