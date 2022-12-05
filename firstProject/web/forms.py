from django import forms

from firstProject.web.models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = ShippingAddress
        exclude = ('customer', 'order', 'profile')
