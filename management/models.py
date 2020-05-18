from django.db import models

# Create your models here.

class student_model(models.Model):
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    sex=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    address=models.CharField(max_length=50)
    message=models.TextField()

    class Meta:
        db_table='student_table'

class faculty_model(models.Model):
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    sex=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    address=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    message=models.TextField()

    class Meta:
        db_table='faculty_table'

class course(models.Model):
    Hindi=models.CharField(max_length=50)
    English=models.CharField(max_length=50)
    Maths=models.CharField(max_length=50) 
    Science=models.CharField(max_length=50)
    SocialScience=models.CharField(max_length=50)

class classes(models.Model):
    faculty=models.ForeignKey(faculty_model, on_delete=models.CASCADE)
    course=models.ForeignKey( course ,on_delete=models.CASCADE)
