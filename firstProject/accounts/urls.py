from django.urls import path

from firstProject.accounts.views import UserLoginView, EditUserProfileView, user_profile, \
    UserLogoutView, UserDashboardView, UserPasswordChangeView, UserRegistrationView
from firstProject.web.views import UserAddressesView, EditUserShippingAddressView, DeleteUserShippingAddressView, \
    AddUserAddressView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('password-change/', UserPasswordChangeView.as_view(), name='change password'),
    path('dashboard/<int:pk>', UserDashboardView.as_view(), name='user dashboard'),
    path('dashboard/profile/edit/<int:pk>', EditUserProfileView.as_view(), name='edit user profile'),
    path('dashboard/addresses/<int:pk>', UserAddressesView.as_view(), name='user shipping addresses'),
    path('dashboard/addresses/edit/<int:pk>', EditUserShippingAddressView.as_view(), name='edit user shipping address'),
    path('dashboard/addresses/delete/<int:pk>', DeleteUserShippingAddressView.as_view(),
         name='delete user shipping address'),
    path('dashboard/addresses/add/', AddUserAddressView.as_view(), name='add user shipping address')
)
