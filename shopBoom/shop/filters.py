import django_filters
from .models import Good, Tag
from django import forms

class GoodFilter(django_filters.FilterSet):
    cost = django_filters.RangeFilter()
    tag = django_filters.ModelChoiceFilter(
        queryset=Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = Good
        fields = {'type':['exact'], 'company':['exact'], 'name':['icontains'],
            }