from django import forms

from firstProject.web.models import ShippingAddress, Product
from firstProject.web.views.products import ProductSizeFormSet


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


class ProductAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Product
        exclude = ('uploaded_by',)

    size_formset = ProductSizeFormSet()


class ProductEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Product
        exclude = ('uploaded_by',)
