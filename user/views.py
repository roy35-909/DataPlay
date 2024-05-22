import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import OuterRef, Subquery
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
    



