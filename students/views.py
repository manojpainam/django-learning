from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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

def greet_participant(request):
    participant = Student.objects.all().values()[2]
    print(participant)
    fname = "Participant"
    if participant:
        fname = participant.get('fname', '')
    context = {
        "firstname" : fname
    }
    return render(request, 'greet_participant.html', context)

def print_all_participants(request):
    participants = Student.objects.all().values()
    context = {
        "participants" : participants
    }
    return render(request, 'show_all_participants.html', context)

'''
Get all users firstname
'''
def get_firstnames(request):
    students_fnames = Student.objects.values_list("fname", flat=True)

    context = {
        "firstnames": students_fnames
    }

    return render(request, "get_firstnames.html", context)