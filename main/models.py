from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator # for rating

class FootballProducts(models.Model):
    name = models.CharField(max_length=120, help_text="Item Name")
    description = models.TextField(help_text="Item Description")
    thumbnail = models.URLField(max_length=330, help_text="Image URL")
    price = models.IntegerField(help_text="Price(rupiah)")
    category = models.CharField(max_length=50, help_text="Item category (ex: Ball, Boots, Shirt, etc)")
    is_featured = models.BooleanField(default=False, help_text="a Featured Item?")
    rating = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(10)],help_text="Drop a rating (0-10)")
    brand = models.CharField(max_length=100, blank=True, null=True, help_text="Brand name(ex: Puma, Under Armour, Nike)")
    stock = models.IntegerField(default=0, help_text="Available stock")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
