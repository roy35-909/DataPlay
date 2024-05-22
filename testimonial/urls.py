
from django.urls import path
from .views import TestimonialAPIView,RetriveTestimonialAPIView

urlpatterns = [

    path('testimonial_list/', TestimonialAPIView.as_view(), name='Testimonial List'),
    path('retrive_testimonial/<int:pk>/', RetriveTestimonialAPIView.as_view(), name='Retrive Testimonial'),

]
