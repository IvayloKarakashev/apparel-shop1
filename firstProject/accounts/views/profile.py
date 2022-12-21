from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.accounts.forms import EditUserProfileForm
from firstProject.accounts.models import Profile
from firstProject.utilities.mixins import PageTitleMixin
from firstProject.web.models import Order, WishList


class EditUserProfileView(LoginRequiredMixin, PageTitleMixin, generic_views.UpdateView):
    page_title = 'Edit Profile'
    model = Profile
    form_class = EditUserProfileForm
    template_name = 'front-end/user-profile-edit.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.request.user)

    def get_success_url(self):
        return reverse_lazy('user dashboard', kwargs={'pk': self.object.pk})


class UserDashboardView(LoginRequiredMixin, PageTitleMixin, generic_views.DetailView):
    page_title = 'Dashboard'
    model = Profile
    template_name = 'front-end/user-dashboard.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(customer_id=self.object.user_id)
        context['wishlist'] = WishList.objects.filter(user_id=self.object.user_id)
        return context
