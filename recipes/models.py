from django.conf import settings
from django.db import models
from django.urls import reverse

from .validators import validate_unit_of_measure
from .utils import number_str_to_float


User = settings.AUTH_USER_MODEL


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id": self.id})


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_to_float, qty_to_float_sucess = number_str_to_float(qty)
        if qty_to_float_sucess:
            self.quantity_as_float = qty_to_float
        else:
            self.quantity_as_float = None
        return super().save(*args, **kwargs)
