from django import forms

from firstProject.accounts.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
