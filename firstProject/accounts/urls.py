from django.urls import path

from firstProject.accounts.views.profile import UserDashboardView, EditUserProfileView
from firstProject.accounts.views.user import UserRegistrationView, UserLoginView, UserLogoutView, UserPasswordChangeView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('password-change/', UserPasswordChangeView.as_view(), name='change password'),
    path('dashboard/<int:pk>', UserDashboardView.as_view(), name='user dashboard'),
    path('dashboard/profile/edit/<int:pk>', EditUserProfileView.as_view(), name='edit user profile')
)
