from django.shortcuts import render

import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import OuterRef, Subquery
from dataplay.base import NewAPIView
from dataplay.response import *
from .models import *
from .serializers import *



class WorkShopGalleryAPIView(NewAPIView):
    permission_classes = []
    serializer_class = WorkShopGallery
    def get(self,request):
        '''
        Hello,\n

        <b>THIS API IS FOR GET ALL  WORKSHOP GALLERY...</b>\n
        THANK YOU .\n
        '''
        gallery = WorkShopGallery.objects.all()
        ser = WorkShopGallerySerializer(gallery,many=True, context={'request':request})
        return s_200(ser)
    

class CourseFeedBackAPIView(NewAPIView):
    permission_classes = []
    serializer_class = CourseFeedback
    def get(self,request):
        '''
        Hello,\n

        <b>THIS API IS FOR GET ALL  Feedback...</b>\n
        THANK YOU .\n
        '''
        feedback = CourseFeedback.objects.all()
        ser = CourseFeedbackSerializer(feedback,many=True, context={'request':request})
        return s_200(ser)
    
class CourseFeedBackByCourseAPIView(NewAPIView):
    permission_classes = []
    serializer_class = CourseFeedback
    def get(self,request, pk):
        '''
        Hello,\n

        <b>THIS API IS FOR GET ALL  <h2> Feedback Of A Single Course </h2>...</b>\n
        <h2>Please Provide Course id in urls</h2> \n
        THANK YOU .\n
        '''
        try:
            course = Course.objects.get(id=pk)
        except (ObjectDoesNotExist):
            return s_404("Course")
        
        feedback = CourseFeedback.objects.filter(course=course)
        ser = CourseFeedbackSerializer(feedback,many=True, context={'request':request})
        return s_200(ser)


class OurTeamAPIView(NewAPIView):
    permission_classes = []
    serializer_class = OurTeamSerializer
    def get(self,request):
        '''
        Hello,\n

        <b>THIS API IS FOR GET "Our Team" List ...</b>\n
        THANK YOU .\n
        '''
        obj = OurTeam.objects.all()
        ser = OurTeamSerializer(obj,many=True, context={'request':request})
        return s_200(ser)