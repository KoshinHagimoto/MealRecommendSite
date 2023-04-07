from django import forms
from .models import Meal


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["name", "imageUrl", "countryOfOrigin", "tag", "description"]
        widgets = {
            "description": forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'name': 'Meal Name',
            'imageUrl': 'Image URL',
            'countryOfOrigin': 'Country of origin',
            'tag': 'Tag',
            'description': 'Description',
        }

