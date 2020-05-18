from django.shortcuts import render,redirect
from management.models import student_model
from management.models import faculty_model
from management.form import student_form
from management.form import faculty_form
from management.form import course
from management.form import classes
from django.http import HttpResponse
# Create your views here.

def index(request):
    list_student=student_model.objects.all()
    list_faculty=faculty_model.objects.all()
    arg={'list_student':list_student,'list_faculty':list_faculty}
    return render(request,'index.html',arg)

def student_upload(request):
    update=student_form()
    if request.method=='POST':
        update=student_form(request.POST, request.FILES)
        if update.is_valid():
            update.save()
            return redirect('index')
        else:
            return HttpResponse(f'Form is in valid...{update.errors}')
    else:
        return render(request,'student1.html',{'update':update})


def faculty_upload(request):
    update=faculty_form()
    if request.method=='POST':
        update=faculty_form(request.POST, request.FILES)
        if update.is_valid():
            update.save()
            return redirect('index')
        else:
            return HttpResponse(f'Form is in valid...{update.errors}')
    else:
        return render(request,'faculty1.html',{'update':update})

def student_update(request,student_id):
    student_id=int(student_id)
    try:
        student_idd=student_model.objects.get(id=student_id)
    except student_model.DoesNotExist:
        return redirect('index')
    form=student_form(request.POST or None,instance=student_idd)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'student1.html',{'update':form})

def faculty_update(request,faculty_id):
    faculty_id=int(faculty_id)
    try:
        faculty_idd=faculty_model.objects.get(id=faculty_id)
    except faculty_model.DoesNotExist:
        return redirect('index')
    form=faculty_form(request.POST or None,instance=faculty_idd)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'faculty1.html',{'update':form})


def student_delete(request,student_id):
    student_id=int(student_id)
    try:
        student_idd=student_model.objects.get(id=student_id)
    except student_model.DoesNotExist:
        return redirect('index')
    student_idd.delete()
    return redirect('index')

def faculty_delete(request,faculty_id):
    faculty_id=int(faculty_id)
    try:
        faculty_idd=faculty_model.objects.get(id=faculty_id)
    except faculty_model.DoesNotExist:
        return redirect('index')
    faculty_idd.delete()
    return redirect('index')


def Attendence(request):
    update=course()
    if request.method=='POST':
        update=course(request.POST, request.FILES)
        if update.is_valid():
            update.save()
            return redirect('index')
        else:
            return HttpResponse(f'Form is in valid...{update.errors}')
    else:
        return render(request,'course.html',{'update':update})


