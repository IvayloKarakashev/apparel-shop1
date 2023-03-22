from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth.models import Group

from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.accounts.forms import UserRegistrationForm, UserLoginForm
from firstProject.utilities.mixins import PageTitleMixin

user_model = get_user_model()
sellers_group = Group.objects.get(name='Sellers')


class UserRegistrationView(PageTitleMixin, generic_views.CreateView):
    page_title = 'Register'
    form_class = UserRegistrationForm
    template_name = 'front-end/user-register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            if obj.is_seller:
                obj.groups.add(sellers_group)
                obj.is_staff = True
                obj.save()
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(PageTitleMixin, auth_views.LoginView):
    page_title = 'Login'
    form_class = UserLoginForm
    template_name = 'front-end/user-login.html'


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserPasswordChangeView(PageTitleMixin, auth_views.PasswordChangeView):
    page_title = 'Change password'
    template_name = 'front-end/user-password-change.html'
