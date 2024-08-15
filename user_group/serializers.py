from rest_framework import serializers
from  django.contrib.auth.models import User,Group

class TestSerializer(serializers.Serializer):
    name= serializers.CharField()
    email = serializers.EmailField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']







