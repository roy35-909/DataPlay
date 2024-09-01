from django.urls import path


from .views import *

urlpatterns = [

    path('workshop_gallery/', WorkShopGalleryAPIView.as_view(), name='Workshop Gallery List'),
    path('course_feedback/', CourseFeedBackAPIView.as_view(), name='Course Feedback List'),
    path('course_feedback/<int:pk>/', CourseFeedBackByCourseAPIView.as_view(), name='Course Feedback by Course List'),
    path('our_team/', OurTeamAPIView.as_view(), name='Our Team List'),


]