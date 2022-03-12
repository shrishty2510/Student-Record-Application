from django.contrib import admin
from . models import Student

@admin.register(Student)
class Useradmin(admin.ModelAdmin):
    list_display = ['id','name','standard','email','password','date']

# Register your models here.
