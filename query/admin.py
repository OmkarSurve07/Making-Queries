from django.contrib import admin
from .models import student , department , entry

# Register your models here.
admin.site.register(student)
admin.site.register(department)
admin.site.register(entry)