from rest_framework import serializers
from django.db.models import QuerySet
from djoser.serializers import UserCreateSerializer
from user.models import Instructor,User
from user.serializers import InstructorSerializer
from .models import Course,CourseContents,FileField,VideoLinks,GoogleDriveLinks,RegisterCourse



## Helper Function 

def is_this_user_purched_this_course(user, course):
    x = RegisterCourse.objects.filter(user__id = user.id, course__id=course.id).exists()
    return x

class CourseSerializer(serializers.ModelSerializer):
    instructors = InstructorSerializer(many=True)
    class Meta:
        model =Course
        fields = '__all__'

class FileFieldSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FileField
        exclude = ('id',)

class WithGoogleDriveLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleDriveLinks
        exclude = ('id',)


class WithOutGoogleDriveLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleDriveLinks
        exclude = ('id','link')


class VideoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLinks
        exclude = ('id',)

class CourseContentSerializerForListing(serializers.ModelSerializer):
    
    class Meta:
        model =CourseContents
        fields = ('id','is_free','title')
    


class CourseContentSerializer(serializers.ModelSerializer):
    files = FileFieldSerializer(many=True)
    video_link = VideoLinkSerializer(many=True)
    google_drive_link = WithGoogleDriveLinkSerializer(many=True)
    class Meta:
        model =CourseContents
        fields = '__all__'


class CourseSerializerWithAllContent(serializers.ModelSerializer):
    contents = serializers.SerializerMethodField()
    instructors = InstructorSerializer(many=True)
    is_purched = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_contents(self,instance):
        user = self.context.get('request')

        contents = CourseContents.objects.filter(course=instance, delete_status = False).order_by('content_order')

        ser = CourseContentSerializerForListing(contents, many=True, context = {'request':self.context.get('request')})
        return ser.data
    
    def get_is_purched(self,instance):
        user = self.context.get('request')
        if user is None:
            return False
        return is_this_user_purched_this_course(user=user.user, course=instance)



class CourseContentSerializerForFree(serializers.ModelSerializer):

    class Meta:
        model =CourseContents
        fields = ("title","is_free",)