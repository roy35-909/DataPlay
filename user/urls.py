from django.urls import path
from .views import *

urlpatterns = [

    path('instructor_list/', InstructorAPIView.as_view(), name='Instructor List'),
    path('mentor_list/', MentorAPIView.as_view(), name='Mentor List'),
    path('retrive_mentor/<int:pk>/', MentorRetriveAPIView.as_view(), name='Retrive Mentor'),
    path('retrive_instructor/<int:pk>/', InstructorRetriveAPIView.as_view(), name='Retrive Instructor'),

]
