from opensource.forms import StudentForm
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from opensource.models import Student, Track

# Create your views here.

def home(request): 
    return HttpResponse("<h1>This is home page</h1>")

def getStudent(request, studentId): 
    student = Student.objects.get(id=studentId)
    context = {'student': student}
    return render(request, 'opensource/student.html', context)

def getAllStudents(request): 
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'opensource/students.html', context)


def newStudent(request): 
    studentForm = StudentForm()
    if request.method == 'POST':
        studentForm = StudentForm(request.POST)
        if studentForm.is_valid():
            studentForm.save()
            return HttpResponseRedirect('/opensource/all')
    context = {'studentForm': studentForm}
    return render(request, 'opensource/newStudent.html', context)



def editStudent(request, studentId): 
    student = Student.objects.get(id = studentId)
    studentForm = StudentForm(instance = student)

    if( request.method == 'POST'):
        studentForm = StudentForm(request.POST, instance=student)
        if studentForm.is_valid():
            studentForm.save()
             
    context = {'studentForm': studentForm}
    return render(request, 'opensource/newStudent.html', context)

def deleteStudent(request, studentId): 
    student = Student.objects.get(id = studentId)
    student.delete()
    return HttpResponseRedirect('/opensource/all')
    