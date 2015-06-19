from django.contrib import admin

# Register your models here.
from .models import Pet,Article

admin.site.register(Pet)
admin.site.register(Article)
