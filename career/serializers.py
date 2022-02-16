from rest_framework import serializers
from rest_framework import fields
from career.models import *

class GetCareerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['id','image', 'designation']


class PostApplicationFormSerializer(serializers.ModelSerializer):
    full_name       = serializers.CharField(required=True)
    email           = serializers.CharField(required=True)
    contact         = serializers.CharField(required=True)
    linkedin_link   = serializers.CharField(required=True)
    resume          = serializers.FileField(required=True)
    designation     = serializers.CharField(required=True)

    class Meta:
        model = ApplicationForm
        fields = ['full_name', 'email','contact','linkedin_link','resume','designation']