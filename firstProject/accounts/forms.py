from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from firstProject.accounts.models import Profile

user_model = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = user_model
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user
        )

        if commit:
            profile.save()

        return user


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Profile
        exclude = ('user',)
