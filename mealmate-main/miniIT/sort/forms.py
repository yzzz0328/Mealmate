from django import forms
from database.models import foodinfo

# This is the form to show the headers in the database
class SortFoodForm(forms.ModelForm):
    class Meta:
        model = foodinfo
        fields = ('name', 'mealtype', 'calories', 'carbs', 'protein','fat', 'fibre', 'size' )



