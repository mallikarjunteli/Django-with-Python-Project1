from django.contrib import admin

# Register your models here.
from eeithapp.models import Student,Course


admin.site.register(Student)
admin.site.register(Course)
