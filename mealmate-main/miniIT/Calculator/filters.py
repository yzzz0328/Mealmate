import django_filters
from django_filters import CharFilter,NumberFilter
from database.models import foodinfo
from django.db.models import When, Case

class foodFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    
    class Meta:
        model = foodinfo
        fields = ['name', 'mealtype', 'calories', 'carbs', 'protein','fat', 'fibre', 'size']
        exclude = ['name', 'calories', 'carbs','protein','fat','fibre', 'size',]