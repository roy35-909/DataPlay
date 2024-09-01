from rest_framework import serializers
from django.db.models import QuerySet
from djoser.serializers import UserCreateSerializer
from .models import *


class WorkShopGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkShopGallery
        fields = '__all__'


class CourseFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFeedback
        fields = '__all__'

        
class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'

        