from rest_framework import serializers
from rest_framework import fields
from home_page.models import *

class GetWatchVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchVideo
        fields = ['video']


class PostSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email','contact']

    def validate_full_name(self, value):
        if value != "":
            return value
        raise serializers.ValidationError("Name Is Required")
        
    def validate_email(self, value):
        if value != "":
            return value
        raise serializers.ValidationError("Email Is Required")
    
    def validate_contact(self, value):
        if value != "":
            return value
        raise serializers.ValidationError("Contact Is Required")


class GetTestmonialsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testmonials
        fields = ['profile_image','full_name','designation','logo','rating','title','description']