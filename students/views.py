from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def greet_student(request):
    return render(request, 'home.html')

def get_all_students(request):
    students = Student.objects.all().values()
    data = {"students" : students}
    return render(request, 'all_students.html', context = data)

def get_details(request, id):
    student = Student.objects.get(id=id)
    data = {"student" : student}
    return render(request, 'details.html', context = data)

def testing(request):
    fruits = ["Mango", "Banana", "Orange", "Kiwi"]
    context = {"fruits" : fruits}
    return render(request, 'testing.html', context)