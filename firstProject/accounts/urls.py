from django.urls import path

from firstProject.accounts.views import UserLoginView, UserRegistrationView, EditUserProfileView, user_profile, \
    UserLogoutView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout', UserLogoutView.as_view(), name='logout user'),
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('profile/', user_profile, name='user profile details'),
    path('profile/edit/', EditUserProfileView.as_view(), name='edit user profile')

)
