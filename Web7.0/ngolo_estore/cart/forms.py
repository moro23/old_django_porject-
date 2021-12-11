#cart/forms.py
from django import forms

PRODUCT_QUALITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices= PRODUCT_QUALITY_CHOICES,
        coerce=int)

    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)