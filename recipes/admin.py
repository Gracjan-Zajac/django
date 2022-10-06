from django.contrib import admin
from .models import Recipe, RecipeIngredient

# Register your models here.


class RecipeIngredientInLine(admin.StackedInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    readonly_fields = ["timestamp", "updated"]
    raw_id_fields = ["user"]
    inlines = [RecipeIngredientInLine]


admin.site.register(Recipe, RecipeAdmin)
