import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import OuterRef, Subquery
from dataplay.base import NewAPIView
from dataplay.response import *
from .models import *
from .serializers import *



class TestimonialAPIView(NewAPIView):
    permission_classes = []
    serializer_class = TestimonialSerializer
    def get(self,request):
        '''
        Hello,\n

        <b>THIS API IS FOR GET ALL TESTIMONIAL LIST...</b>\n
        THANK YOU .\n
        '''
        testimonial = Testimonial.objects.all().order_by('order')
        ser = TestimonialSerializer(testimonial,many=True, context={'request':request})
        return s_200(ser)
    
class RetriveTestimonialAPIView(NewAPIView):
    permission_classes = []
    serializer_class = TestimonialSerializer
    def get(self,request,pk):
        '''
        Hello,\n

        <b>THIS API IS Retrive TESTIMONIAL </b>\n
        THANK YOU .\n
        '''
        try:
            testimonial = Testimonial.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return s_404('testimonial')
        ser = TestimonialSerializer(testimonial,context={'request':request})
        return s_200(ser)

