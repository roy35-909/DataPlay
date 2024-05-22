from django.urls import path
from .views import CourseAPIView,RetriveCourseAPIView,RetriveCourseContentAPIView

urlpatterns = [

    path('course_list/', CourseAPIView.as_view(), name='Course List'),
    path('retrive_course_with_contents/<int:pk>/', RetriveCourseAPIView.as_view(), name='Retrive Course'),
    path('retrive_course_content/<int:pk>/', RetriveCourseContentAPIView.as_view(), name='Retrive Course Content '),
]
