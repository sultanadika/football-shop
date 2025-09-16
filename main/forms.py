from django import forms
from .models import FootballProducts

class FootballProductsForm(forms.ModelForm):
    class Meta:
        model = FootballProducts
        fields = ["name", "description", "category", "brand", "price", "thumbnail", "is_featured"]
  