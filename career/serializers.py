from rest_framework import serializers
from rest_framework import fields
from career.models import *

class GetCareerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['id','image', 'designation']


class PostApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = ['full_name', 'email','contact','linkedin_link','resume','designation']

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

    def validate_linkedin_link(self, value):
        if value != "":
            return value
        raise serializers.ValidationError("Linkedin Link Is Required") 
    
    def validate_resume(self, value):
        if value != "":
            return value
        raise serializers.ValidationError("Resume Is Required")

    def validate_designation(self, value):
        if value != "":
            return value
        raise serializers.ValidationError("Designation Is Required") 