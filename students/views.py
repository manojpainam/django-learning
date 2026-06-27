from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from django.db.models import Q


def greet_student(request):
    return render(request, 'home.html')

def get_all_students(request):
    #students = Student.objects.all().values()

    #ASEC - can also order by different values like fname
    #students = Student.objects.all().order_by('fname').values()

    #DESC - descending order
    students = Student.objects.all().order_by('-fname').values()
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

'''
Get student by Id by using the Query set methods
'''
def get_stduent_by_id(request, id):
    #filter.values will give the query set which we can't loop in query set in the template
    student = Student.objects.filter(id=id).first()
    data = {
        "student" : student
    }
    if student:
        return render(request, "details.html", context = data)
    
    return render(request, "404.html")


'''
Query set filter 
'''
#AND : this function will let's you to search the student by knowing their name and id
def get_stduent_by_id_and_firstname(request, id, fname):
    # we are using fname__iexact exact in URL we can't pass the caps
    student = Student.objects.filter(fname__iexact=fname, id=id).first()
    if student:
        return render(request, "details.html", context = {"student" : student})
    
    return render(request, "404.html")

#OR
def get_student_by_fname_or_lname(request, fname, lname):
    student = Student.objects.filter(Q(fname__iexact=fname) | Q(lname__iexact=lname)).first()

    #can also use fname__startwith

    if student:
        return render(request, "details.html", context = {"student" : student})
    
    return render(request, "404.html")

def load_static(request):
    fruits = ['apple', 'banana', 'cherry']
    
    if fruits:
        return render(request, "fruits.html", context = {"fruits" : fruits})
    
    return render(request, "404.html")