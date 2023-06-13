from django import forms
from database.models import foodinfo

class ChooseFoodForm(forms.ModelForm):

    class Meta:
        model = foodinfo
        fields = ['name', 'mealtype', 'calories', 'carbs', 'protein','fat', 'fibre', 'size']

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddFoodForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int,
                                label="Quantity",)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
