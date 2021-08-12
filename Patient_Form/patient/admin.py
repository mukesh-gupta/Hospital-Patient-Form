from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Patient


class PersonDetailAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateTimeField: {'input_formats': ('%m/%d/%Y',)},
    }
admin.site.register(Patient,PersonDetailAdmin)