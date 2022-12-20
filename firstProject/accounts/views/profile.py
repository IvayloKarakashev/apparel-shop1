from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.accounts.models import Profile
from firstProject.utilities.mixins import PageTitleMixin
from firstProject.web.models import Order, WishList


class EditUserProfileView(LoginRequiredMixin, PageTitleMixin, generic_views.UpdateView):
    page_title = 'Edit Profile'
    model = Profile
    template_name = 'front-end/user-profile-edit.html'
    fields = ('first_name', 'last_name', 'gender')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.request.user)

    def get_success_url(self):
        return reverse_lazy('user dashboard', kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         # obj.user = request.user
    #         # obj.order = order
    #
    #         obj.save()

    # def get_object(self, queryset=None):
    #     return self.model.objects.get(pk=self.request.user.pk)


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
