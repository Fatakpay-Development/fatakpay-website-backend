from rest_framework import serializers
from rest_framework import fields
from contact_us.models import *



class GetContactUsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'message']

class PostContactUsSerializer(serializers.ModelSerializer):
    full_name   = serializers.CharField(required=True)
    email       = serializers.CharField(required=True)
    message     = serializers.CharField(required=True, max_length=None, min_length=None,)

    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'message']

class GetffplContactUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ffplContactUser
        fields = ['full_name', 'email', 'message']

class PostffplContactUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    message = serializers.CharField(required=False, max_length=None, min_length=None,allow_blank=True, allow_null=True)

    class Meta:
        model = ffplContactUser
        fields = ['full_name', 'email', 'message']