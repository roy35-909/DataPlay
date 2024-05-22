from rest_framework import serializers
from django.db.models import QuerySet
from djoser.serializers import UserCreateSerializer
from .models import User
class UserCreateSerializers(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','first_name','last_name','password',)

    def update(self, instance, validated_data):
        # Somehow save instance with new quiz_data
        print(validated_data)
        return instance
