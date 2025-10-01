from django import forms
from .models import FootballProducts


class FootballProductsForm(forms.ModelForm):
    class Meta:
        model = FootballProducts
        fields = ["name", "description", "category", "brand", "price", "thumbnail", "is_featured"]

class CarForm(forms.Form):
    name = forms.CharField(label="name", max_length=255)
    brand = forms.CharField(label="brand", max_length=255)
    stock = forms.IntegerField(label="stock: ")
