from django.contrib.auth import views as auth_views, get_user_model, login

from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.accounts.forms import UserRegistrationForm
from firstProject.utilities.mixins import PageTitleMixin

user_model = get_user_model()


class UserRegistrationView(PageTitleMixin, generic_views.CreateView):
    page_title = 'Register'
    form_class = UserRegistrationForm
    template_name = 'front-end/user-register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserLoginView(PageTitleMixin, auth_views.LoginView):
    page_title = 'Login'
    template_name = 'front-end/user-login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserPasswordChangeView(auth_views.PasswordChangeView):
    pass
