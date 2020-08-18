from django.contrib import admin
from .models import Category, Place, Congestion


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Place)
admin.site.register(Congestion)
