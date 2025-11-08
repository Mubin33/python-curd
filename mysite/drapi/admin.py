 
from django.contrib import admin
from . models import Aiquest
# Register your models here. 

@admin.register(Aiquest)
class AiquestAdmin(admin.ModelAdmin):
    list_display = ['id', 'teachers_name', 'course_name', 'course_duration','sit']