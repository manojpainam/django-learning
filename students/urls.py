from django.urls import path
from . import views

urlpatterns = [
    path('greet_student/', views.greet_student, name='students'),
    path('get_all_students/', views.get_all_students, name='get_all_students'),
    path('student/<int:id>', views.get_details, name="get_details"),
    path('testing/', views.testing, name="testing"),
    path('greet_participant/', views.greet_participant, name='greet_participant'),
    path('all/', views.print_all_participants, name='print_all_participants')
]