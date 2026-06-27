from django.urls import path
from . import views

urlpatterns = [
    path('greet_student/', views.greet_student, name='students'),
    path('get_all_students/', views.get_all_students, name='get_all_students'),
    path('student/<int:id>', views.get_details, name="get_details"),
    path('testing/', views.testing, name="testing"),
    path('greet_participant/', views.greet_participant, name='greet_participant'),
    path('all/', views.print_all_participants, name='print_all_participants'),
    path('get_fristnames', views.get_firstnames, name='get_fristnames'),
    path('get_student/<id>', views.get_stduent_by_id, name="get_student_by_id"),
    path('get_student/<id>/<fname>', views.get_stduent_by_id_and_firstname, name="get_stduent_by_id_and_firstname"),
    path('get_student_by_fname_or_lname/<fname>/<lname>', views.get_student_by_fname_or_lname, name="get_student_by_fname_or_lname"),
    path('get_fruits', views.load_static, name="load_static")

]