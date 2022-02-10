from rest_framework import serializers
from rest_framework import fields
from career.models import *

class GetCareerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['image', 'designation']


class PostApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = ['full_name', 'email','contact','linkedin_link','resume','designation']
