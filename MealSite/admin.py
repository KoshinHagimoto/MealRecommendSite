from django.contrib import admin
from .models import Tag, Meal, MealRating


admin.site.register(Tag)
admin.site.register(Meal)
admin.site.register(MealRating)

