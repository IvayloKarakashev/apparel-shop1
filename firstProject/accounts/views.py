from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth import forms as auth_forms
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.accounts.forms import UserRegistrationForm
from firstProject.accounts.models import Profile

user_model = get_user_model()


class UserRegistrationView(generic_views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)

    context = {
        'profile': profile
    }

    return render(request, 'accounts/profile.html', context)


class UserProfileDetailsView(generic_views.DetailView):
    model = Profile
    template_name = 'accounts/profile.html'


class EditUserProfileView(generic_views.UpdateView):
    model = Profile
    # form_class = ProfileEditForm
    template_name = 'accounts/profile_edit.html'
    fields = ('first_name', 'last_name', 'image')
    success_url = reverse_lazy('user profile details')

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.request.user.pk)
