from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('student_upload',views.student_upload,name="student_upload"),
    path('faculty_upload',views.faculty_upload,name="faculty_upload"),
    path('update/<int:student_id>',views.student_update),
    path('update1/<int:faculty_id>',views.faculty_update),
    path('delete/<int:student_id>',views.student_delete),
    path('delete1/<int:faculty_id>',views.faculty_delete),
]
