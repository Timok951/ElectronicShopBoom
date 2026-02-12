from django import forms
from .models import Type, Good, Rate


"""
class FindForm(forms.Form):
    name = forms.CharField()

class FilterForm(forms.Form):
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, empty_label="Type", widget=forms.Select(attrs={'placeholder': 'Country'}))


"""


class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = [
            "name",
            "amount",
            "cost",
            "image",
            "max_voltage",
            "capacity",
            "resistance",
            "article",
            "type",
            "company",
            "tag",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ["rating", "comment"]
