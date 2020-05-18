from django.contrib import admin
from management.models import student_model
from management.models import faculty_model

# Register your models here.
admin.site.register(student_model),
admin.site.register(faculty_model)