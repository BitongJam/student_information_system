from django.contrib import admin
from . models import Students

# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display =("id","name")

admin.site.register(Students,StudentsAdmin)
