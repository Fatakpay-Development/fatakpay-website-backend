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
