from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()
