from django.contrib.auth import views as auth_views, get_user_model, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_views

from firstProject.accounts.forms import UserRegistrationForm
from firstProject.accounts.models import Profile
from firstProject.web.models import Order, WishList

user_model = get_user_model()


class UserRegistrationView(generic_views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'front-end/register.html'
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


class UserPasswordChangeView(auth_views.PasswordChangeView):
    pass


def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)

    context = {
        'profile': profile
    }

    return render(request, 'accounts/profile.html', context)


# class UserProfileDetailsView(generic_views.DetailView):
#     model = Profile
#     template_name = 'accounts/profile.html'


class EditUserProfileView(generic_views.UpdateView):
    model = Profile
    template_name = 'front-end/user-profile-edit.html'
    fields = ('first_name', 'last_name', 'gender')

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


class UserDashboardView(generic_views.DetailView):
    model = Profile
    template_name = 'front-end/user-dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(customer_id=self.object.user_id)
        context['wishlist'] = WishList.objects.filter(user_id=self.object.user_id)
        return context
