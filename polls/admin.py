from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question

# This tells Django that Question objects have an admin interface
admin.site.register(Question)