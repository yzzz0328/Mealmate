import django_filters

from .models import *

class EntryFilter(django_filters.FilterSet):
    class Meta:
        model = Entry
        fields = {
            'author': ['icontains']
        }