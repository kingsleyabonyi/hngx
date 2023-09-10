from django.urls import path
from .views import student_info


urlpatterns = [
    path('student/', student_info, name='student_info')
]