from rest_framework import serializers
from rest_framework import fields
from contact_us.models import *



class GetContactUsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'message']

class PostContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'message']
        
    def validate_full_name(self, value):
        if value != "":
            return value
        raise serializers.ValidationError("Name Is Required")
        
    def validate_email(self, value):
        if value != "":
            return value
        raise serializers.ValidationError("Email Is Required")
    
    def validate_message(self, value):
        if value != "":
            return value
        raise serializers.ValidationError("Message Is Required")

   