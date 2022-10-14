from django.urls import path

from firstProject.accounts.views import UserLoginView, UserRegistrationView, UserProfileView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('profile/', UserProfileView.as_view(), name='user profile'),

)
