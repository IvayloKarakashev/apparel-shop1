from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model, password_validation
from django.contrib.auth.forms import UsernameField

from firstProject.accounts.models import Profile

user_model = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'name': 'name3', 'id': 'emailname'})
    )

    first_name = forms.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={'name': 'name', 'id': 'name'})
    )

    last_name = forms.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={'name': 'name2', 'id': 'name2'})
    )

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'name': 'pass', 'id': 'pass'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'name': 'pass', 'id': 'compass'}),
        strip=False,
        help_text='Enter the same password as before, for verification.',
    )

    class Meta:
        model = user_model
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = False

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )

        if commit:
            profile.save()

        return user


class UserLoginForm(auth_forms.AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'name': 'name', 'id': 'name', 'autofocus': False})
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'name': 'pass', 'id': 'pass', 'autocomplete': 'current-password'}),
    )


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Profile
        exclude = ('user',)
