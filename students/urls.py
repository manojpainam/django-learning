from django.urls import path
from . import views

urlpatterns = [
    path('greet_student/', views.greet_student, name='members')
]