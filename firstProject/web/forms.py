from django import forms

from firstProject.accounts.models import Profile
from firstProject.web.models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = ShippingAddress
        exclude = ('customer', 'order', 'profile')
        help_texts = {
            'label': 'Note: The Label field is optional. Labeling the address '
                     'can help you choose address easily when making future orders. (E.g "Home", "Work")'
        }
