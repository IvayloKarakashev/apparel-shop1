from django.urls import path

from firstProject.accounts.views import UserLoginView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
)
