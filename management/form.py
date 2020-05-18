from django.forms import ModelForm

from .models import student_model
from .models import faculty_model
from .models import course
from .models import classes
class student_form(ModelForm):
    class Meta:
        model=student_model
        fields=['name','father_name','email','address','sex','message']
    

class faculty_form(ModelForm):
    class Meta:
        model=faculty_model
        fields=['name','father_name','email','course','sex','address','qualification','message'] 

class course(ModelForm):
    class Meta:
        model=course
        fields=['Hindi','English','Maths','Science','SocialScience']

class classes(ModelForm):
    class Meta:
        model=classes
        fields=['faculty','course']