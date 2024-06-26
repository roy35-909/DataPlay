from rest_framework import serializers
from django.db.models import QuerySet
from djoser.serializers import UserCreateSerializer
from user.models import Instructor,User
from user.serializers import InstructorSerializer
from .models import Course,CourseContents,FileField,VideoLinks

class CourseSerializer(serializers.ModelSerializer):
    instructors = InstructorSerializer(many=True)
    class Meta:
        model =Course
        fields = '__all__'

class FileFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileField
        exclude = ('id',)


class VideoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLinks
        exclude = ('id',)

class CourseContentSerializerForListing(serializers.ModelSerializer):

    class Meta:
        model =CourseContents
        fields = ('id','is_free','title',)

class CourseContentSerializer(serializers.ModelSerializer):
    files = FileFieldSerializer(many=True)
    video_link = VideoLinkSerializer(many=True)
    class Meta:
        model =CourseContents
        fields = '__all__'


class CourseSerializerWithAllContent(serializers.ModelSerializer):
    contents = serializers.SerializerMethodField()
    instructors = InstructorSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_contents(self,instance):
        free_contents = CourseContents.objects.all().order_by('content_order')
        ser = CourseContentSerializerForListing(free_contents, many=True, context = {'request':self.context.get('request')})
        return ser.data
