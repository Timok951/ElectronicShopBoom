import django_filters
from .models import Good, Tag, Type, Company
from django import forms

class GoodFilter(django_filters.FilterSet):
    cost = django_filters.RangeFilter()
    tag = django_filters.ModelChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    type = django_filters.ModelChoiceFilter(
        queryset=Type.objects.all(),
        empty_label="All types",
        widget=forms.RadioSelect,
        label="Type",
        error_messages={"invalid_choice": "Category not found"},
    )
    company = django_filters.ModelChoiceFilter(
        queryset=Company.objects.all(),
        empty_label="All brands",
        widget=forms.RadioSelect,
        label="Company"
    )
    
    class Meta:
        model = Good
        fields = {'type':['exact'], 'company':['exact'], 'name':['icontains'],
            }
