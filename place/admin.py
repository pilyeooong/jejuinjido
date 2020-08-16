from django.contrib import admin
from .models import Category, Place, Congestion


admin.site.register(Place)
admin.site.register(Category)
admin.site.register(Congestion)
