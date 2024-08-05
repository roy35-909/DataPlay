import json

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import OuterRef, Subquery
from rest_framework.permissions import IsAuthenticated

from dataplay.base import NewAPIView
from dataplay.response import *

from .models import *
from .serializers import *


class InstructorAPIView(NewAPIView):
    permission_classes = []
    serializer_class = InstructorSerializer

    def get(self, request):
        '''
        Hello,\n
        <b>This api is for Listing  all Instructor.\n</b>\n
        THANK YOU .\n
        '''

        instructor = Instructor.objects.all().order_by('order')
        ser = InstructorSerializer(instructor,many=True, context = {'request':request})
        return s_200(ser)
    

class InstructorRetriveAPIView(NewAPIView):
    permission_classes = []
    serializer_class = InstructorSerializer

    def get(self, request,pk):
        '''
        Hello,\n
        <b>This api is for Listing  all Instructor.\n</b>\n
        THANK YOU .\n
        '''

        instructor = Instructor.objects.get(id=pk)
        ser = InstructorSerializer(instructor,context = {'request':request})
        return s_200(ser)
    

class MentorAPIView(NewAPIView):
    permission_classes = []
    serializer_class = MentorSerializer

    def get(self, request):
        '''
        Hello,\n
        <b>This api is for Listing  all Instructor.\n</b>\n
        THANK YOU .\n
        '''

        mentor = Mentor.objects.all().order_by('order')
        ser = MentorSerializer(mentor,many=True, context = {'request':request})
        return s_200(ser)
   

class MentorRetriveAPIView(NewAPIView):
    permission_classes = []
    serializer_class = MentorSerializer

    def get(self, request,pk):
        '''
        Hello,\n
        <b>This api is for Listing  all Instructor.\n</b>\n
        THANK YOU .\n
        '''

        mentor = Mentor.objects.get(id=pk)
        ser = MentorSerializer(mentor, context = {'request':request})
        return s_200(ser)
    


class StudentProfileAPIView(NewAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer


    def post(self,request):
        '''
        Hello,\n
        This api is for Student Profile Registration .\n\n
        <h1> Authentication Required for Access This API  </h1> \n\n
        <h1> No need to pass the user object on request body.  </h1> \n\n
        THANK YOU .\n
        '''
        data = request.data 

        fields = ['bio','linkedin','mobile_no','what_are_you_currently_doing',
                  'college_name','highest_degree_of_study','year_of_study','home_town_city',
                  'birthday','how_did_you_find_us']
        try:
            userprofile = Students.objects.get(user = request.user)
        except(ObjectDoesNotExist):
            userprofile = Students.objects.create(user = request.user)
        for i in fields:
            if i in data:
                setattr(userprofile,i,data[i])
        if "profile_pic" in data:
            userprofile.profile_pic = request.FILES['profile_pic']
        userprofile.save()
        ser = StudentSerializer(userprofile, context = {'request':request})
        return s_200(ser)
    

class GetStudentProfileAPIView(NewAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer


    def get(self,request):
        '''
        Hello,\n
        This api is for Get Student Profile \n\n
        <h1> Authentication Required for Access This API  </h1> \n\n
        THANK YOU .\n
        '''
        try:
            userprofile = Students.objects.get(user = request.user)
        except(ObjectDoesNotExist):
            userprofile = Students.objects.create(user = request.user)

        ser = StudentSerializer(userprofile, context = {'request':request})
        return s_200(ser)
    

