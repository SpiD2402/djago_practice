from rest_framework import serializers
from django.forms import  model_to_dict
from .models import Language
from django.contrib.auth.models import User

from  user_group.serializers import UserSerializer

class LanguageSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False, read_only = True)
    user_id=serializers.IntegerField(write_only=True)
    #user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)



    class Meta:
        model = Language
        fields = '__all__'

    #Primera Forma
    """def to_representation(self, instance):
        data=super().to_representation(instance)
        user= model_to_dict(instance.user)
        data['user'] = user
        return data"""
    #Segunda Forma
