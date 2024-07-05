import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import OuterRef, Subquery
from dataplay.base import NewAPIView
from dataplay.response import *
from .models import *
from .serializers import *



class CourseAPIView(NewAPIView):

    permission_classes = []
    serializer_class = CourseSerializer


    def get(self, request):
        '''
        Hello,\n
        <b>THIS API IS FOR GET ALL Course LIST...</b>\n
        THANK YOU .\n
        '''
        courses = Course.objects.all().order_by('course_order')
        ser = CourseSerializer(courses,many=True, context ={'request':request})
        return s_200(ser)


class RetriveCourseAPIView(NewAPIView):

    permission_classes = []
    serializer_class = CourseSerializerWithAllContent


    def get(self, request,pk):
        '''
        Hello,\n
        <b>THIS API IS FOR Retrive Course With Content \n</b>\n
        THANK YOU .\n
        '''
        try:
            course = Course.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return s_404('course')
        
        ser = CourseSerializerWithAllContent(course, context ={'request':request})
        return s_200(ser)
    

class RetriveCourseContentAPIView(NewAPIView):

    permission_classes = []
    serializer_class = CourseContentSerializer

    def is_this_user_purched_this_course(self,user, course):

        x = RegisterCourse.objects.filter(user__id = user.id, course__id=course.id).exists()
        return x

    def get(self, request,pk):
        '''
        Hello,\n
        <b>THIS API IS FOR Retrive Course Content. If you but this course you can access all content otherwise you can only retrive the free content. \n</b>\n
        THANK YOU .\n
        '''
        try:
            course_content = CourseContents.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return s_404('Course Content')
        
        if self.is_this_user_purched_this_course(request.user,course_content.course):
            ser = CourseContentSerializer(course_content, context ={'request':request})
        else:
            return Response({"msg":"Please Purchase This Course."}, status=status.HTTP_401_UNAUTHORIZED)
        return s_200(ser)
    
