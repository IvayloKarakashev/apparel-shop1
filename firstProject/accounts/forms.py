from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from firstProject.accounts.models import Profile

User = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
