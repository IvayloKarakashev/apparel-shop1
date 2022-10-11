from django.urls import path

from firstProject.web.views import HomeView, CategoriesView, SingleCategoryView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>', SingleCategoryView.as_view(), name='single category'),
    # path('products/details/<int:pk>', ProductDetailsView.as_view(), name='product details'),
)
