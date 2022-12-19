from django.urls import path

from firstProject.accounts.views.user_address import select_address, enter_new_address
from firstProject.web.views.generic import home_view
from firstProject.web.views.order import cart, checkout, finalize_order, update_item_quantity, add_to_cart, clear_items, \
    OrderSuccessView, OrderTrackingView
from firstProject.web.views.products import CategoriesView, ProductsView, ProductDetailsView
from firstProject.web.views.static import FAQView, TermsAndConditionsView, AboutView
from firstProject.web.views.wishlist import WishListView, update_wishlist

urlpatterns = (
    path('', home_view, name='index'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>', ProductsView.as_view(), name='products'),
    path('products/details/<int:pk>', ProductDetailsView.as_view(), name='product details'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('cart/', cart, name='cart'),
    path('select-address/', select_address, name='select address'),
    path('enter-new-address/', enter_new_address, name='enter new address'),
    path('checkout/', checkout, name='checkout'),
    path('finalize-order/', finalize_order, name='finalize order'),
    path('update-item-quantity/', update_item_quantity, name='update item quantity'),
    path('add-to-cart/', add_to_cart, name='add to cart'),
    path('clear-items/', clear_items, name='clear items'),
    path('update-wishlist/', update_wishlist, name='update wishlist'),
    path('order-success/<int:pk>', OrderSuccessView.as_view(), name='order success'),
    path('order-tracking/<int:pk>', OrderTrackingView.as_view(), name='order tracking'),
    path('faq', FAQView.as_view(), name='faq'),
    path('terms', TermsAndConditionsView.as_view(), name='terms and conditions'),
    path('about', AboutView.as_view(), name='about us'),
)
