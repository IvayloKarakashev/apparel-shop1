from django.urls import path

from firstProject.web.views import CategoriesView, ProductsView, ProductDetailsView, cart, update_item, \
    checkout, OrderSuccessView, home_view, WishListView, update_wishlist, OrderTrackingView, FAQView, \
    TermsAndConditionsView, AboutView

urlpatterns = (
    path('', home_view, name='index'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>', ProductsView.as_view(), name='products'),
    path('products/details/<int:pk>', ProductDetailsView.as_view(), name='product details'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update-item/', update_item, name='update item'),
    path('update-wishlist/', update_wishlist, name='update wishlist'),
    path('order-success/<int:pk>', OrderSuccessView.as_view(), name='order success'),
    path('order-tracking/<int:pk>', OrderTrackingView.as_view(), name='order tracking'),
    path('faq', FAQView.as_view(), name='faq'),
    path('terms', TermsAndConditionsView.as_view(), name='terms and conditions'),
    path('about', AboutView.as_view(), name='about us'),
    # path('test/', TestView.as_view(), name='test view')
)
