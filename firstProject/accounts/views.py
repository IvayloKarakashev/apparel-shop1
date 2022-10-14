from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth import forms as auth_forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.accounts.models import Profile

user_model = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = user_model
        fields = ('username',)


class UserRegistrationView(generic_views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserProfileView(generic_views.DetailView):
    model = Profile
    template_name = 'accounts/profile.html'


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
