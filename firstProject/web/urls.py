from django.urls import path

from firstProject.web.views import CategoriesView, ProductsView, ProductDetailsView, cart, update_item_quantity, \
    checkout, OrderSuccessView, home_view, WishListView, update_wishlist, OrderTrackingView, FAQView, \
    TermsAndConditionsView, AboutView, add_to_cart, select_address, enter_new_address, finalize_order

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
    # path('select-address/', select_address, name='select address'),
    path('update-wishlist/', update_wishlist, name='update wishlist'),
    path('order-success/<int:pk>', OrderSuccessView.as_view(), name='order success'),
    path('order-tracking/<int:pk>', OrderTrackingView.as_view(), name='order tracking'),
    path('faq', FAQView.as_view(), name='faq'),
    path('terms', TermsAndConditionsView.as_view(), name='terms and conditions'),
    path('about', AboutView.as_view(), name='about us'),
    # path('test/', TestView.as_view(), name='test view')
)
