from django.shortcuts import render
from django.http import HttpResponse


def greet_student(request):
    return render(request, 'home.html')