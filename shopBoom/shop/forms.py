from django import forms
from .models import Type


"""
class FindForm(forms.Form):
    name = forms.CharField()

class FilterForm(forms.Form):
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, empty_label="Type", widget=forms.Select(attrs={'placeholder': 'Country'}))


"""
