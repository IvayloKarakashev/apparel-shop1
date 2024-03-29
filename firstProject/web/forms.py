from django import forms
from django.forms import inlineformset_factory, TextInput

from firstProject.web.models import ShippingAddress, Product, ProductSize


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


ProductSizeFormSet = inlineformset_factory(
    Product,
    ProductSize,
    fields=('name',),
    # can_delete=True,
    extra=5,
    widgets={
        'name': TextInput(attrs={'class': 'form-control-sm', 'style': 'width: 50px'})
    }
)


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
