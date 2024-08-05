from rest_framework import serializers
from django.db.models import QuerySet
from user.models import Instructor,User,Mentor,Students



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class InstructorSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = Instructor
        fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Mentor
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = Students
        fields = '__all__'

