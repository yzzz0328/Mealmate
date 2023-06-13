import django_filters
from django_filters import CharFilter, NumberFilter
from database.models import foodinfo
from django.db.models import When, Case

# This code allows the users to search the foods that they want to choose

class FoodFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

# This function allows the users to filter the food by mealtype and the code is extended in the HTML/CSS file    
    class Meta:
        model = foodinfo
        fields = ('name', 'mealtype', 'calories', 'carbs', 'protein','fat', 'fibre', 'size' )
        exclude = ['name', 'calories', 'carbs','protein','fat','fibre', 'size']
