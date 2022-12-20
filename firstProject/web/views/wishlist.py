import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import generic as generic_views
from firstProject.utilities.mixins import PageTitleMixin
from firstProject.web.models import WishList, Product


class WishListView(PageTitleMixin, LoginRequiredMixin, generic_views.ListView):
    page_title = 'Wishlist'
    model = WishList
    template_name = 'front-end/wishlist.html'

    def get_queryset(self):
        return WishList.objects.filter(user=self.request.user)
